from colored import fg, bg, attr
import datetime
import os
from objects import context
import logging

class Colors:
    PINK 		= '{}'.format(fg(171))
    BLUE 		= '{}'.format(fg(4))
    GREEN 		= '{}'.format(fg(118))
    YELLOW 		= '{}'.format(fg(226))
    RED 		= '{}'.format(fg(1))
    ENDC 		= '{}'.format(attr(0))
    BOLD 		= '{}'.format(attr('bold'))


def printAscii():
    print("""                                                                                           ,.                                   
                                                                                     /@@@@@@@@@@@(                              
                                                                                   .@@@@@@@@@@@@@@@,                            
                                                                                   @@@@@@@@@@@@@@@@@                            
                                                                                   @@@@@@@@@@@@@@@@@                            
                                                                                    @@@@@@@@@@@@@@@,                            
                                                                                     ,@@@@@@@@@@@*                              
                                                      ..*/(#%%%@@@@%%%%((*,.                                                    
                                     ./%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&%/.                                   
                           ./&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%,                          
                    /@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%.                  
             *%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&*            
       ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%*.                               ,(%@@@@@@@@@@@@@@@&.      
  (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&/.                                                            .,/#@@&, 
        .#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%.                                                                            
               .&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.                                                                                 
                    &@@@@@@@@@@@@@@@@@@@@@*                                                                                     
                       @@@@@@@@@@@@@@@@*                                                                                        
                         #@@@@@@@@@@&                                                                                           
                           &@@@@@@&                                                                                             
                            .@@@@                                                                                               
                              @#                                                                                                
""")

def write(string:str,  noNL:bool=False)->None:
    if  noNL:
        print(string, end="")
    else:
        print(string)


def writeColored(string:str, color:Colors, noNL:bool=False)->None:
    if  noNL:
        print(f"{color}{string}{Colors.ENDC}", end="")
    else:
        print(f"{color}{string}{Colors.ENDC}")

def writeFailure():
    writeColored("Failure", Colors.RED)

def writeSuccess():
    writeColored("Success", Colors.GREEN)

def writeCaution():
    writeColored("Caution", Colors.YELLOW)

def caut(string):
    x = datetime.datetime.now()
    print("{}[{}] CAUTION - {}{}".format(Colors.YELLOW, x.strftime("%Y-%m-%d %H:%M:%S"), string, Colors.ENDC))

def chat(message, fro, to):
    x = datetime.datetime.now()
    print("{}[{}] CHAT - ({} => {}) :  {}{}".format(Colors.BLUE, x.strftime("%Y-%m-%d %H:%M:%S"), fro, to, message, Colors.ENDC))

def info(string):
    x = datetime.datetime.now()
    print("{}[{}] INFO{} - {}".format(Colors.GREEN, x.strftime("%Y-%m-%d %H:%M:%S"),  Colors.ENDC, string))

def debug(string):
    x = datetime.datetime.now()
    print("{}[{}] DEBUG{} - {}".format(Colors.PINK, x.strftime("%Y-%m-%d %H:%M:%S"),  Colors.ENDC, string))

def error(string):
    x = datetime.datetime.now()
    print("{}[{}] ERROR - {}{}".format(Colors.RED, x.strftime("%Y-%m-%d %H:%M:%S"),  string, Colors.ENDC))

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


class CustomHandler(logging.Handler):
    def emit(self, record):
        log_entry = self.format(record)
        if record.levelno == logging.INFO:
            info(log_entry)
        elif record.levelno == logging.ERROR:
            error(log_entry)
        elif record.levelno == logging.DEBUG:
            debug(log_entry)

logging_handler = CustomHandler()
logging_handler.setLevel(logging.DEBUG if context.debug else logging.INFO)
formatter = logging.Formatter("[%(asctime)s] %(levelname)s in %(module)s: %(message)s")