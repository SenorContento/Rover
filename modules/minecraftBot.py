__author__ = 'SenorContento' #Me: Brandon Gomez
__module__ = 'minecraft'
__purpose__ = 'communicate with Minecraft servers'

#Imports
#################################################################################################
try:
  import settings
except ImportError:
  print("ImportError! Cannot import settings (This is a Rover library)!")

try:
  import modules
except ImportError:
  print("ImportError! Cannot import modules (This is a Rover library)!")

try:
  from minecraft import authentication
except ImportError:
  print("ImportError! Cannot import authentication from minecraft (This is from a pyCraft library)!")

try:
  from minecraft.exceptions import YggdrasilError
except ImportError:
  print("ImportError! Cannot import YggdrasilError from minecraft.exceptions (This is from a pyCraft library)!")

try:
  from minecraft.networking.connection import Connection
except ImportError:
  print("ImportError! Cannot import Connection from minecraft.networking.connection (This is from a pyCraft library)!")

try:
  from minecraft.networking.packets import ChatMessagePacket, ChatPacket # Should I split this?
except ImportError:
  print("ImportError! Cannot import ChatMessagePacket and ChatPacket from minecraft.networking.packets (This is from a pyCraft library)!")

try:
  from minecraft.compat import input
except ImportError:
  print("ImportError! Cannot import input from minecraft.compat (This is from a pyCraft library)!")

try:
  import json
except ImportError:
  print("ImportError! Cannot import json!")

try:
  import database
except ImportError:
  print("ImportError! Cannot import database (This is a Rover library)!")

#Functions
#################################################################################################
def init():
  debug = settings.retrieveVariable("debug") # Should I turn this into a global or load it outside of a function?

  try:
    database.addTable("minecraft")
  except:
    print("Cannot create table in (minecraft) Database!")

  if debug:
    print("Setting Variables!")
    print("Checking if online mode!")

  try: # Sets variable "offline"
    offline = settings.setVariable("minecraft.offline", settings.readConfig('Minecraft', 'offline'))
    offline = settings.readBoolean(offline, False) # This converts the string to boolean (if valid)
    settings.setVariable("minecraft.offline", offline) # Sets variable to be type boolean
  except:
    settings.setVariable("minecraft.offline", False)
    print("Assuming Online mode!!!")

  if debug:
    print("Checking if I should connect right now!")

  try: # Sets variable "connect"
    connect = settings.setVariable("minecraft.connect", settings.readConfig('Minecraft', 'connect'))
    connect = settings.readBoolean(connect, False) # This converts the string to boolean (if valid)
    settings.setVariable("minecraft.connect", connect) # Sets variable to be type boolean
  except:
    settings.setVariable("minecraft.connect", False)
    print("Assuming not autoconnecting!")

  if debug:
    print("Setting username!")

  try: # Sets variable "username"
    username = settings.setVariable("minecraft.username", settings.readConfig('Minecraft', 'username'))
  except:
    print("Cannot import username!")

  if debug:
    print("Setting password!")

  try:  # Sets variable "password" if in online mode
    offline = settings.retrieveVariable("minecraft.offline")
    if not offline:
      password = settings.setVariable("minecraft.pw", settings.readConfig('Minecraft', 'pw'))
  except:
    print("Cannot import password!")

  if debug:
    print("Setting Server!")

  try: # Sets variable "server"
    connect = settings.retrieveVariable("minecraft.connect")
    if connect:
      settings.setVariable("minecraft.server", settings.readConfig('Minecraft', 'server'))
  except:
    print("Cannot import server!")

  if debug:
    print("Setting port!")

  try: # Sets variable "port"
    connect = settings.retrieveVariable("minecraft.connect")
    if connect:
      settings.setVariable("minecraft.port", int(settings.readConfig('Minecraft', 'port')))
  except:
    settings.setVariable("minecraft.port", 25565)
    print("Cannot import port! Setting to default port number 25565!")

  connect = settings.retrieveVariable("minecraft.connect")
  if connect:
    if debug:
      print("Attempting to Connect to server!")
    #try:
    username = settings.retrieveVariable("minecraft.username")
    server = settings.retrieveVariable("minecraft.server")
    port = settings.retrieveVariable("minecraft.port")

    if not settings.retrieveVariable("minecraft.offline"):
      password = settings.retrieveVariable("minecraft.pw") # Move this one for online mode only!
      if debug:
        print("Connecting to server (online-mode)!")
      connectServer(server, port, username, password) # Connects to the server if connect mode is enabled
    else:
      if debug:
        print("Connecting to server (offline-mode)!")
      connectServerOffline(server, port, username)
    #except:
      #None
      #print("Cannot connect to server!") # Please be more descriptive

#################################################################################################
debug = settings.retrieveVariable("debug") # Should I turn this into a global or load it outside of a function?
def handle(messageData): # This function can only get chat messages, so I don't have to worry about handling other messages!
  # This is a mess! Btw, Rover can pick up its own chat messages! Be careful not to put Rover into a loop!
  messageJSON = json.loads(messageData.json_data)

  try:
    database.insertValues("minecraft", str(messageJSON))
  except:
    print("Cannot insert values into (minecraft) database!")

  if debug:
    print("Got message JSON: %s!" % messageJSON)

  try:
    message = messageJSON['extra'][0]['text'] # This reads player messages!
    #message = messageJSON['with'][1]['extra'][0]['text'] # This reads server and RCON messages!
    if debug:
      print("Message: %s!" % message)

    output = modules.allcommands("commands", message)
    if output is not None: # Send reply back to server!
      packet = ChatPacket()
      packet.message = output
      connection.write_packet(packet)
  except KeyError:
    if debug:
      print("Cannot parse message right now! JSON: %s" % messageData.json_data)

#################################################################################################
def connectServer(server, port, username, password):
  global connection # Need better way of passing variable!
  debug = settings.retrieveVariable("debug") # Should I turn this into a global or load it outside of a function?
  
  if debug:
    print("Connecting to online-mode server \"%s:%s\" under the username \"%s\"!" % (server, port, username))

  try:
    auth_token = authentication.AuthenticationToken()
    auth_token.authenticate(username, password)
    connection = Connection(server, port, auth_token)
    connection.connect()
  except:
    print("Cannot connect to server (Online Mode)!")

  try:
    connection.register_packet_listener(handle, ChatMessagePacket) # Sets up function to handle chat messages!
  except:
    print("Cannot register function to listen for chat messages!")

#################################################################################################
def connectServerOffline(server, port, username):
  global connection # Need better way of passing variable!
  debug = settings.retrieveVariable("debug") # Should I turn this into a global or load it outside of a function?
  
  if debug:
    print("Connecting to offline-mode server \"%s:%s\" under the username \"%s\"!" % (server, port, username))

  try:
    connection = Connection(server, port, username)
    connection.connect()
  except:
    print("Cannot connect to server (Offline Mode)!")

  try:
    connection.register_packet_listener(handle, ChatMessagePacket) # Sets up function to handle chat messages!
  except:
    print("Cannot register function to listen for chat messages!")
#################################################################################################
if __name__ == "__main__":
  print("Please don't run me directly! I am module %s!\nMy purpose is to %s!" % (__module__, __purpose__))
