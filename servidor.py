import socket
import os

def manejar(conexion, clienteN):
    print("Manejando conexion a cliente {0}".format(clienteN))
    mensaje = "Conexion establecida, bienvenido"
    conexion.send(mensaje.encode())
    conexion.close()
    print("Mensaje enviado a cliente {0}, finalizando conexion".format(clienteN))
    
def iniciarConexion():
    print("Iniciando conexion...")
    PUERTO = 5000
    ON_HEROKU = os.environ.get('ON_HEROKU')
    if ON_HEROKU:
        PUERTO = int(os.environ.get('PORT', 5000))
    print("Puerto encontrado -> "+str(PUERTO))
    DIRECCION = '0.0.0.0'
    #DIRECCION = '127.0.0.1'
    #DIRECCION = socket.gethostname()
    conexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conexion.bind((DIRECCION, PUERTO))
    conexion.listen(5)
    print("Conexion finalizada -> " + str(socket.gethostbyname(DIRECCION)))
    return conexion
    

servidor = iniciarConexion()
clientes = 0
while True:
    cliente, direccion = servidor.accept()
    clientes += 1
    print("Nueva conexion: Clientes -> {0}".format(clientes))
    print("Direccion: "+ str(direccion))
    manejar(cliente, clientes)