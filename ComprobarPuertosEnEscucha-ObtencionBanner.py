#!/usr/bin/env python
from random import randint
from ipaddress import IPv4Address
from socket import socket, AF_INET, SOCK_STREAM, setdefaulttimeout, getfqdn
from os import path
from optparse import OptionParser
from dns import resolver, reversename
from sys import exit


def isOpenPort(host, port, timeout):
    setdefaulttimeout(timeout)
    template = "{0:16}{1:3}{2:40}"

    # Intentamos establecer una conexión a un puerto, en caso positivo realizamos las funciones pertinentes
    try:
        # Definimos conexión
        #   AF_INET: Representa conjunto (host, port)
        #   SOCK_STREAM: Establece protocolo de la conexión TCP
        connection = socket(AF_INET, SOCK_STREAM)

        # Establecemos par de dirección IP y puerto
        connection.connect((host, port))

        # Obtenemos el banner y lo parseamos
        connection.send(b'HEAD / HTTP/1.0\r\n\r\n')
        banner = connection.recv(50)#Tamaño de la respuesta a imprimir (BANNER)

        # Imprimimos mensaje Puerto abierto junto a la dirección IPv4
        print(template.format(host, '->', 'Open Port'))

        # Adaptamos salto de línea a HTML
        aux = str(banner).replace('\\r\\n', '<br/>')

        # Obtenemos banner eliminando carácteres especiales del principio y del final
        banner = aux[2:len(aux) - 3]
        print(banner)
        # Cerramos la conexión
        connection.close()

        return True

    except Exception as e:
        print(template.format(host, '->', 'Closed Port: (' + str(e) + ')'))
        connection.close()
        return False

#isOpenPort(ip_host_remoto,puerto_host_remoto, tiempo_de_espera)
print ("prueba1", isOpenPort('192.168.1.1',80,10))
print ("prueba2", isOpenPort('192.168.1.1',443,10))
print ("prueba3", isOpenPort('192.168.1.1',8080,10))
print ("prueba4", isOpenPort('192.168.1.1',4050,10))
print ("prueba5", isOpenPort('192.168.1.1',37010,10))
print ("prueba6", isOpenPort('192.168.1.1',6969,10))
