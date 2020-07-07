import socket
sock = socket.socket()
sock.connect(('en.wikipedia.org', 80))

for line in (
    "GET /wiki/List_of_HTTP_header_fields HTTP/1.1",
    "Host: en.wikipedia.org",
    "Connection: close",
):
    sock.send(str(line + "\r\n").encode())
sock.send("\r\n".encode())

while True:
    content = sock.recv(1024)
    if content:
        print (content)
    else:
        break