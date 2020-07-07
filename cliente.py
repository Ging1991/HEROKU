import socket
import json

# Leer respuesta del servidor
def comunicar(conexion):
    print("Esperando respuesta del server...")
    respuesta = conexion.recv(1024)
    print(str(respuesta))
    conexion.close()
    print("Finalizando conexion.")
    

def crearConexion():
    print("Creando conexion...")
    DIRECCION = "pythonservercarlos.herokuapp.com"
    DIRECCION = "localhost"
    PUERTO = 443
    PUERTO = 5000
    mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mi_socket.connect((DIRECCION, PUERTO))
    print("Conexion establecida.")
    return mi_socket


mi_socket = crearConexion()
comunicar(mi_socket)