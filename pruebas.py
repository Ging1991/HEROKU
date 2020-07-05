import socket
import json

DIRECCION = "172.18.17.53"
DIRECCION = "localhost"
DIRECCION = "python-server-carlos.herokuapp.com"
PUERTO = 5000
PUERTO = 80
print(socket.getaddrinfo(DIRECCION, PUERTO))

