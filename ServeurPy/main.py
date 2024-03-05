import websockets
import asyncio
from flask import Flask
from multiprocessing import Process
from helpers import general_helper
import time
from objects import context
from helpers import console
from api.ws.websocket import main
WEBSOCKET_PORT = 8555
HTTP_PORT = 8080

console.clear()
console.printAscii()

context.app = Flask(__name__)
console.info("Importing all http handlers")
general_helper.register_all_handlers("api/http/")
console.info("Finish import task")

console.info("Websocket listening on Port " + str(WEBSOCKET_PORT))
console.info("Flask listening on Port " + str(HTTP_PORT))


def startWebsocket():
    start =  websockets.serve(main, "localhost", WEBSOCKET_PORT)
    asyncio.get_event_loop().run_until_complete(start)
    asyncio.get_event_loop().run_forever()

def startFlask():
    context.app.logger.addHandler(console.logging_handler)
    context.app.run('0.0.0.0', port=HTTP_PORT, debug=context.debug)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    p1 = loop.run_in_executor(None, func=startFlask)
    p2 = loop.run_in_executor(None, func=startWebsocket)
    try:
        while True:
            time.sleep(.2)
            pass
    except KeyboardInterrupt:
        console.caut("Keyboard Interrupt")
        p1.cancel()
        p2.cancel()
    finally:
        console.info("goodbye")