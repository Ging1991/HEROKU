import socket
import json

DIRECCION = "python-server-carlos.herokuapp.com"
PUERTO = 80
print(socket.getaddrinfo(DIRECCION, PUERTO))

