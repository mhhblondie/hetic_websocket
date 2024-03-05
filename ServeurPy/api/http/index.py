from objects import context
from flask import request, abort

@context.app.route("/")
def index():
    return "<p>Hello, World!</p>"

@context.app.route("/users/<channel>/messages")
def ch(channel):
    token = request.headers.get('token', None)
    if token is None or context.users.get(token, None) is None:
        abort(403)

    user = context.users[context.users.get(token)]
    user2 = context.users.get(channel)
    if user2 is None:
        user2 = context.user_manager.get_user(channel)
    if user2 is None:
        abort(404)
    return context.message_manager.get_messages_between(user, user2)

@context.app.route("/users")
def get_channels():
    token = request.headers.get('token', None)
    if token is None or context.users.get(token, None) is None:
        abort(403)
    user = context.users.get(token)
    u = context.user_manager.get_users() 
    del u[user.id]
    return u
    