#!/usr/bin/env python

# WS server example

import asyncio
import websockets
import os

async def hello(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")

    greeting = f"Hello {name}!"

    await websocket.send(greeting)
    print(f"> {greeting}")


# Seteo constantes 
ON_HEROKU = os.environ.get('ON_HEROKU')
PUERTO = 5000
DIRECCION = '127.0.0.1'
if ON_HEROKU:
    PUERTO = int(os.environ.get('PORT', 5000))
    DIRECCION = '0.0.0.0'
    #DIRECCION = socket.gethostname()


start_server = websockets.serve(hello, DIRECCION, PUERTO)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
print("iniciando server")