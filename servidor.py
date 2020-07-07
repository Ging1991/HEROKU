import socket
import os

# Seteo constantes
ON_HEROKU = os.environ.get('ON_HEROKU')
PUERTO = 5000
DIRECCION = '127.0.0.1'
if ON_HEROKU:
    PUERTO = int(os.environ.get('PORT', 5000))
    DIRECCION = '0.0.0.0'
    #DIRECCION = socket.gethostname()

# Creo el socket servidor
print("Iniciando servidor")
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((DIRECCION, PUERTO))
servidor.listen(5)
print("Servidor en linea -> " + str(socket.gethostbyname(DIRECCION)))
    
# Ciclo principal del servidor
cantidad = 0
while True:
    cliente, direccion = servidor.accept()
    cantidad += 1
    print("Nueva conexion: Clientes -> {0}".format(cantidad))
    print("Direccion: "+ str(direccion))
    
    # Manejando conexion de cliente
    mensaje = "Conexion establecida, bienvenido"
    cliente.sendall(mensaje.encode())
    cliente.close()
    print("Mensaje enviado a cliente {0}, finalizando conexion".format(cantidad))