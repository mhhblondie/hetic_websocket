import os
import json
import time
from helpers.general_helper import *
from objects import context
from os import path
from objects.user import User
from objects.message import Message
from datetime import datetime, timedelta
import bcrypt
from helpers import console
class UserManager:
    def __init__(self, folder) -> None:
        p = path.join(os.getcwd(), folder) 
        self.folder = p
        if not path.exists(p):
            os.mkdir(p)
        userFolder = path.join(p, "users")
        self.userFolder = userFolder
        if not path.exists(userFolder):
            os.mkdir(userFolder)
        self.user_cache = path.join(self.folder, "users.json")
        if not path.exists(self.user_cache):
            with open(self.user_cache, "w") as f:
                f.write("{}")

    def register_user(self, username, password) -> User:
        id = os.listdir(self.userFolder) + 1
        userfold = path.join(self.user_path, id)
        os.mkdir(userfold)
        u = User({
            "id" : id,
            "username" : username,
            "pw_hash": password
        })
        self.save_user(u)
        return u

    def get_users(self):
        with open(self.user_cache, "r") as f:
            jsond = json.loads(f.read())
        return jsond

    def login_user(self, username:str, password:str) -> User:
        id = self.get_id(username)
        if id == -1:
            return (False, None)
            console.caut(f'username "{username}" tried to login but do not exists')
        user = self.get_user(id)
        if user.check_password(password):
            console.info(f'user {user.username} logged in')
            return (True, self.gen_token(user))
        else:
            console.caut(f'user {user.username} tried to log but failed with password')
        
    def gen_token(self, user:User):
        found = False
        while not found:
            token = randomString(32)
            if not any([s.token == token for s in context.users.values()]):
                found = True
        user.token = token
        context.users[token] = user
        return token
    
    def cron(self):
        todel:list['User'] = []
        for user in context.users.values():
            if user.websocket is not None and not user.websocket.closed:
                user.last_activity = datetime.now()
            elif user.websocket.closed:
                user.websocket = None
            
            dif = datetime.now - user.last_activity

            if dif >= timedelta(minutes=2):
                todel.append(user)
        for user in todel:
            console.caut(f'user {user.username} has timed out and has been disconnected')
            del context.users[user.token]
            user.token = None

    def logout(user:User):
        console.info(f'user {user.username} logged out')
        del context.users[user.token]
        user.token = None


    def get_id(self, username:str) -> int:
        with open(self.user_cache) as f:
            jsond:dict = json.loads(f.read())
        return jsond.get(username.lower(), -1)
        
    
    def user_messages_path(self, user:User):
        return path.join(self.folder, "users", user.id, "messages.json")

    def user_path(self, id):
        return path.join(self.folder, "users", id, "user.json")

    def get_user(self, id):
        if id in context.users.keys():
            return context.users[id]
        with open(self.user_path(id)) as f:
            j = json.loads(f.read())
            return User(j)

    def save_user(self, user:User):
        data = {
            "id" : user.id,
            "username" : user.username,
            "pw_hash": bcrypt.hashpw(user.password_hash, bcrypt.gensalt())
        }
        string = json.dumps(data)
        with open(self.user_cache, "r") as f:
            jsond = json.loads(f.read())
            jsond[user.username.lower()] = user.id
        with open(self.user_cache, "w") as f:
            string = json.dumps(jsond)
            f.write(string)
        
        with open(self.user_path(user.id), 'w') as f:
            f.write(string)

        
    

    