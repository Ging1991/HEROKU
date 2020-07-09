import asyncio
import websockets
import os

async def saludar(conexion, path):
    respuesta = await conexion.recv()
    print("<< {0}".format(respuesta))
    saludo = '{"tipo":"servidor", "mensaje":"Se ha conectado exitosamente"}'
    await conexion.send(saludo)
    print(">> {0}".format(saludo))

# Seteo constantes 
ON_HEROKU = os.environ.get('ON_HEROKU')
PUERTO = 5000
DIRECCION = '127.0.0.1'
if ON_HEROKU:
    PUERTO = int(os.environ.get('PORT', 5000))
    DIRECCION = '0.0.0.0'

print("Iniciando server...1")
start_server = websockets.serve(saludar, DIRECCION, PUERTO)
print("Iniciando server...2")
asyncio.get_event_loop().run_until_complete(start_server)
print("Iniciando server...3")
asyncio.get_event_loop().run_forever()
print("Server iniciado.")