import asyncio
import websockets

local = True
DIRECCION = "ws://localhost:5000"
if not local:
    DIRECCION = "ws://pythonservercarlos.herokuapp.com:80"

async def saludar():
    async with websockets.connect(DIRECCION) as websocket:
        nombre = input("¿Cual es tu nombre?")
        await websocket.send(nombre)
        print(">> {0}".format(nombre))
        respuesta = await websocket.recv()
        print(">> {0}".format(respuesta))

asyncio.get_event_loop().run_until_complete(saludar())