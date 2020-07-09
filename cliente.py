#!/usr/bin/env python

# WS client example

import asyncio
import websockets

async def saludar():
    uri = "ws://pythonservercarlos.herokuapp.com:80"
    #uri = "ws://localhost:5000"
    async with websockets.connect(uri) as websocket:
        nombre = input("¿Cual es tu nombre?")
        await websocket.send(nombre)
        print(">> {0}".format(nombre))
        respuesta = await websocket.recv()
        print(">> {0}".format(respuesta))

asyncio.get_event_loop().run_until_complete(saludar())