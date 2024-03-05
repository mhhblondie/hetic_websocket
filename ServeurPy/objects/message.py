from objects.user import User
from datetime import datetime
class Message:
    def __init__(self, user:User, content:str, time:datetime, channel:str):
        self.user:User = None
        self.content:str = None
        self.time:datetime = None
        self.channel:str = None