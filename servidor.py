import threading
import socket
import json
import os

enEspera = dict()
enEspera["junio"] = -1
enEspera["DICIEMBRE"] = -1

# Hilo para comunicar a los jugadores entre salas
def comunicar(servidor, cliente1, cliente2):
    while True:
        # Le envio a cliente2 el mensaje de cliente1
        respuesta = cliente1.recv(1024)
        cliente2.send(respuesta)

        # Le envio a cliente1 el mensaje de cliente2
        respuesta = cliente2.recv(1024)
        cliente1.send(respuesta)

def crearSala(servidor, cliente1, cliente2):
    hilo = threading.Thread(target=comunicar, args=(servidor, cliente1, cliente2))
    hilo.start()

def manejarRecepcion(servidor, cliente):
    
    # Envio un mensaje de que se ha establecido la conexion
    mensaje = dict()
    mensaje["tipo"] = "servidor"
    mensaje["contenido"] = "Conexion establecida, bienvenido"
    prep = str(mensaje).replace("'", '"')
    cliente.send(prep.encode())

    # Recibo un mensaje con su nombre y el de su oponente
    respuesta = cliente.recv(1024).decode()
    print("Debug:--"+str(respuesta)+"--")
    if str(respuesta) == "":
        print("Ha recibido una respuesta incorrecta")
        return

    respuesta_json = json.loads(respuesta)
    if respuesta_json["tipo"] != "cliente":
        print("Tipo de mensaje no reconocido: " + respuesta_json["tipo"])
        return
    usuario = respuesta_json["usuario"]
    oponente = respuesta_json["oponente"]

    # Es el host asi que lo agrego a la lista de espera
    if (oponente == ""):
        print("Host agregado a la lista de espera..." + usuario)
        enEspera[usuario] = cliente
        mensaje["contenido"] = "Ha entrado en la sala de espera..."
        prep = str(mensaje).replace("'", '"')
        cliente.send(prep.encode())
        return


    # Si no lo es lo agrego a la sala
    if oponente in enEspera.keys():
        print("Agregando a la sala de duelo..." + usuario)
        mensaje["contenido"] = "Hemos encontrado a su rival, en breve empezara el duelo"
        prep = str(mensaje).replace("'", '"')
        cliente.send(prep.encode())

        crearSala(servidor, enEspera[oponente], cliente)
        del enEspera[oponente]
        return

    mensaje["contenido"] = "No se encontro su oponente: " + oponente
    prep = str(mensaje).replace("'", '"')
    cliente.send(prep.encode())
    cliente.close()

def iniciarConexion():
    print("Iniciando conexion...")
    PUERTO = 5000
    ON_HEROKU = os.environ.get('ON_HEROKU')
    if ON_HEROKU:
        PUERTO = int(os.environ.get('PORT', 5000))
    DIRECCION = '0.0.0.0'
    DIRECCION = "python-server-carlos.herokuapp.com"
    conexion = socket.socket()
    conexion.bind((DIRECCION, PUERTO))
    conexion.listen(10)

    hostname = socket.gethostname()
    ## getting the IP address using socket.gethostbyname() method
    ip_address = socket.gethostbyname(hostname)
    print("Conexion finalizada..." + str(ip_address))
    return conexion
    

servidor = iniciarConexion()
cantidad = 0
while True:
    cliente, direccion = servidor.accept()
    cantidad+=1
    print("Nueva conexion establecida: {0}".format(cantidad))
    print("Direccion: "+ str(direccion))
    manejarRecepcion(servidor, cliente)