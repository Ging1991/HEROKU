import socket
import json

# Leer respuesta del servidor
def leerServidor(conexion):
    print("Esperando respuesta del server...")
    respuesta = conexion.recv(1024)
    for i in respuesta:
        print(str(i))



    if str(respuesta.decode()) == "":
        print("Ha recibido una respuesta vacia")
    respuesta = conexion.recv(1024)
    if str(respuesta.decode()) == "":
        print("Ha recibido una respuesta vacia")
    respuesta = conexion.recv(1024)
    if str(respuesta.decode()) == "":
        print("Ha recibido una respuesta vacia")
        
    print("Debug: --" + str(respuesta) +"--")
    print("Debug: --" + respuesta.decode() +"--")
    respuesta = conexion.recv(1024).decode()
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
    print("Iniciando conexion...")
    DIRECCION = "python-server-carlos.herokuapp.com"
    #DIRECCION = "localhost"
    PUERTO = 80
    #PUERTO = 5000
    mi_socket = socket.socket()
    mi_socket.connect((DIRECCION, PUERTO))

    #envio basura a ver si la lee
    mensaje = dict()
    mensaje["contenido"] = "Basura 1"
    prep = str(mensaje).replace("'", '"')
    mi_socket.send(prep.encode())
    mensaje["contenido"] = "Basura 2"
    prep = str(mensaje).replace("'", '"')
    mi_socket.send(prep.encode())
    mensaje["contenido"] = "Basura 3"
    prep = str(mensaje).replace("'", '"')
    mi_socket.send(prep.encode())





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