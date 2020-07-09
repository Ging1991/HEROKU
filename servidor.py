import asyncio
import websockets
import os

async def saludar(websocket, path):
    nombre = await websocket.recv()
    print("<< {0}".format(nombre))
    saludo = "Hola {0}!".format(nombre)
    await websocket.send(saludo)
    print(">> {0}".format(saludo))

# Seteo constantes 
ON_HEROKU = os.environ.get('ON_HEROKU')
PUERTO = 5000
DIRECCION = '127.0.0.1'
if ON_HEROKU:
    PUERTO = int(os.environ.get('PORT', 5000))
    DIRECCION = '0.0.0.0'

start_server = websockets.serve(saludar, DIRECCION, PUERTO)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
print("iniciando server")