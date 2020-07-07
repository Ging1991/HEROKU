import socket
import json

# Seteo constantes
local = True
DIRECCION = "localhost"
PUERTO = 5000
if not local:
    DIRECCION = "pythonservercarlos.herokuapp.com"
    PUERTO = 80

# Creo la conexion
print("Creando conexion...")
mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mi_socket.connect((DIRECCION, PUERTO))
print("Conexion establecida.")

# Leer respuesta del servidor y finalizar
print("Esperando respuesta del servidor...")
respuesta = mi_socket.recv(1024)
print("-"+str(respuesta)+"-")
mi_socket.close()
print("Conexion finalizada.")