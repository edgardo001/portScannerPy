#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime

# Por medio de la consola, insetar IP del servidor a escanear.
#remoteServer    = input("Ingrese el host a escanear: ")

# Indicar IP en duro
remoteServer = '192.168.1.1'
# Indicar puertos a verificar.
ports = [9090,9091,42000,51020,80,443,22]

remoteServerIP  = socket.gethostbyname(remoteServer)

# Imprimir banner con información sobre qué host estamos a punto de escanear
print ("-" * 60)
print ("Espere, escaneando el host remoto", remoteServerIP)
print ("-" * 60)

# Compruebe a qué hora comenzó el escaneo
t1 = datetime.now()

# Usar la función de rango para especificar puertos (aquí escaneará todos los puertos entre 1 y 1024) descomentar "for port in range(1,1024):"
# Usar el escaneo de puertos especificos especificados en la variable "ports", descomentar "for port in ports:"
try:
    #for port in range(1,1024): #Scann a un rango determinado. Se puede descomentar y comentar la linea "for port in ports:"    
    for port in ports: #Scann a puertos especificos en la lista "ports"
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print ("Port {}: 	 Open".format(port))
        else:
            print ("Port {}: 	 Close".format(port))
        sock.close()

except KeyboardInterrupt:
    print ("Presionar Ctrl+C")
    sys.exit()
except socket.gaierror:
    print ('El nombre de host no se pudo resolver. Terminando proceso')
    sys.exit()
except socket.error:
    print ("No se pudo conectar al servidor")
    sys.exit()

# Comprobando el tiempo de nuevo
t2 = datetime.now()

# Calcula la diferencia de tiempo, para ver cuánto tiempo llevó ejecutar el script
total =  t2 - t1

# Imprimir la información en la pantalla
print ('Escaneo completado en: ', total)
