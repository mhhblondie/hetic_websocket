import bcrypt
from datetime import datetime
import websockets
class User:
    def __init__(self, dic:dict):
        self.id = dic["id"]
        self.websocket:websockets.WebSocketClientProtocol = None
        self.password_hash = dic["pw_hash"]
        self.username = dic["username"]
        self.token = None
        self.last_activity:datetime = datetime.now()

    def check_password(self, password:str) -> bool:
        return bcrypt.checkpw(password, self.password_hash)
        