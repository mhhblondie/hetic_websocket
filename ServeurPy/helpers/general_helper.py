import random
import string
import os
import traceback
from helpers import console
def randomString(length:int=8)->string:
    out = str()
    for i in range(length):
        out += random.choice(string.ascii_letters + string.digits)
    return out

def register_all_handlers(path):
    files = os.listdir(os.path.join(os.getcwd(), path))
    
    baseimport = path.replace("/", ".")
    baseimport.strip(".")
    for file in files:
        if file.endswith(".py"):
            file = file.replace(".py", "")
            console.writeColored("loading Handler {}{}{} ...".format(console.Colors.ENDC,file, console.Colors.BLUE), console.Colors.BLUE, True)
            try:
                __import__(baseimport + file)
                console.writeSuccess()
            except Exception as e:
                console.error(traceback.format_exc())
                console.writeFailure()