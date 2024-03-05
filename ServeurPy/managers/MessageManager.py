import os
import json
import time
from objects import context
from os import path
from objects.user import User
from objects.message import Message
from datetime import datetime

class MessageManager:
    def __init__(self, folder) -> None:
        p = path.join(os.getcwd(), folder) 
        self.folder = p
        self.messages_path = path.join(self.folder, "messages.json")
        if not path.exists(self.messages_path):
            with open(self.messages_path, "w") as f:
                f.write("[]")

    def save_message(self, message:Message):
        with open(self.messages_path) as f:
            jsond:list = json.loads(f.read())

        jsond.append({
            "user": message.user.id,
            "content": message.content,
            "time" : message.time.timestamp(),
            "channel": message.channel
        })

        with open(self.messages_path, "w") as f:
            f.write(json.dumps(sorted(jsond, key=lambda k: k['time'])))

    def get_messages_user(self, user:User):
        with open(self.messages_path) as f:
            json:list = json.loads(f.read())
        return [Message(self.get_user(s["user"]), s["content"], datetime.fromtimestamp(s["time"]), s["channel"]) for s in json if user.id == s["user"]]

    def get_messages_between(self, user1:User, user2:User):
        with open(self.messages_path) as f:
            json:list = json.loads(f.read())
        return [Message(self.get_user(s["user"]), s["content"], datetime.fromtimestamp(s["time"]), s["channel"]) for s in json if (
            (user1.id == s["channel"] and s["user"] == user2.id) 
            or 
            (user2.id == s["channel"] and s["user"] == user1.id)
            )]
            