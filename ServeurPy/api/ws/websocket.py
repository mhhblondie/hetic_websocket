import websockets
from helpers import console
from objects import context
from objects.user import User
from datetime import datetime
from objects.message import Message
import json

async def main(websocket:websockets.WebSocketClientProtocol, path):
    token = websocket.request_headers.get("token", None)
    if token is None or context.users.get(token, None) is None:
        websocket.close(403)
        return
    user = context.users.get(token)
    user.websocket = websocket
    try:
        async for message in websocket:
            handle(message, user)
    except websockets.exceptions.ConnectionClosed as e:
        print("A client just disconnected")
    finally:
        user.websocket = None

def handle(message: str, emitter:User):
    jsond = json.loads(message)
    _type = jsond["type"]
    match _type:
        case "message":
            handle_message(jsond, emitter)
        case other:
            console.caut(f"unrecognize type {other}")

def handle_message(message_json:dict, emitter:User):
    message = Message(emitter, message_json["content"], datetime.fromtimestamp(float(message_json["time"])), message_json["channel"])
    target = context.user_manager.get_user(int(message.channel))
    if target is not None and target.websocket is not None:
        target.websocket.send(json.dumps(message_json))
    context.message_manager.save_message(message)