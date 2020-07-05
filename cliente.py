import socket
import json

#mi_socket = socket.socket()
DIRECCION = "https://python-server-carlos.herokuapp.com/"
PUERTO = 17995
print(socket.getaddrinfo(DIRECCION, PUERTO))


# Leer respuesta del servidor
def leerServidor(conexion):
    respuesta = conexion.recv(1024).decode()
    #print("Debug: " + respuesta)
    respuesta_json = json.loads(respuesta)
    if respuesta_json["tipo"] != "servidor":
        print("Tipo de respuesta incorrecto: " + respuesta_json["tipo"])
        return
    print(respuesta_json["contenido"])

# Leer respuesta del cliente
def leerCliente(conexion):
    respuesta = conexion.recv(1024).decode()
    #print("Debug: " + respuesta)
    respuesta_json = json.loads(respuesta)
    if respuesta_json["tipo"] != "cliente":
        print("Tipo de respuesta incorrecto: " + respuesta_json["tipo"])
        return
    print(respuesta_json["cartas"])

# Creo la conexion y devuelvo el socket
def crearConexion():
    DIRECCION = "localhost"
    DIRECCION = "https://python-server-carlos.herokuapp.com/"
    PUERTO = 5000
    PUERTO = 17995
    mi_socket = socket.socket()
    mi_socket.connect((DIRECCION, PUERTO))
    print("Intentando conectar...")
    leerServidor(mi_socket)
    return mi_socket
    
# Envio el mensaje con mi nombre y el de mi oponente
def presentacion(conexion):
    mensaje = '{"tipo":"cliente","usuario" : "cliente1","oponente" : ""}'
    mensaje = '{"tipo":"cliente","usuario" : "cliente2","oponente" : "cliente1"}'
    mi_socket.send(mensaje.encode())
    leerServidor(conexion)

# Envio mis cartas
def cartas(conexion):
    mensaje = '{"tipo":"cliente","cartas" : [1,2,3]}'
    mi_socket.send(mensaje.encode())
    leerCliente(conexion)

mi_socket = crearConexion()
presentacion(mi_socket)
cartas(mi_socket)
mi_socket.close()