import socketserver  #importo el modulo del server
import os

#creo la clase Handler
class MiTcpHandler(socketserver.BaseRequestHandler):
    #se va a llamar en cada coneccion
    def handle(self):
        #self.oracion= self.request.recv(1024).strip() #recibo data
        
        #self.num = len(self.oracion)# cuento los caracters "1234abc" self.num = 7
        print("Enviando mensaje")
        self.request.send("Esta conectado".encode()) #le mando el numero de caracteres
        
        
def main():
    print ("Tutorial 53 Servidores")
    
    # Seteo constantes 
    ON_HEROKU = os.environ.get('ON_HEROKU')
    PUERTO = 5000
    DIRECCION = '127.0.0.1'
    if ON_HEROKU:
        PUERTO = int(os.environ.get('PORT', 5000))
        DIRECCION = '0.0.0.0'
        #DIRECCION = socket.gethostname()

    #creo el servidor
    server1 = socketserver.TCPServer((DIRECCION,PUERTO), MiTcpHandler)
    
    print ("server corriendo")
    server1.serve_forever() # ande hasta q cierre el programa

main()