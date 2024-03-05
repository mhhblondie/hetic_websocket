from managers.UserManager import UserManager
from managers.MessageManager import MessageManager
from objects.user import User
from flask import Flask

cache_folder = ".cache"

user_manager = UserManager(cache_folder)
message_manager = MessageManager(cache_folder)
users:dict['str', 'User'] = {}
app:Flask = None

debug = False