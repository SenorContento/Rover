__author__ = 'SenorContento' #Me: Brandon Gomez
__module__ = 'irc'
__purpose__ = 'communicate with irc servers'

#Imports
#################################################################################################
try:
  import settings
except ImportError:
  print("ImportError! Cannot import settings (This is a Rover library)!")

try:
  import database
except ImportError:
  print("ImportError! Cannot import database (This is a Rover library)!")

try:
  import modules
except ImportError:
  print("ImportError! Cannot import modules (This is a Rover library)!")

try:
  import socket
except ImportError:
  print("ImportError! Cannot import socket!")

try:
  import sys
except ImportError:
  print("ImportError! Cannot import sys!")

irc = socket.socket()

#Functions
#################################################################################################
def init():
  irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  try:
    database.addTable("irc")
  except:
    print("Cannot create table in (irc) Database!")

  try:
    server = settings.setVariable("irc.server", settings.readConfig('IRC', 'server'))
  except:
    print("You need a server to connect to!!!")

  try:
    port = settings.setVariable("irc.port", settings.readConfig('IRC', 'port'))
  except:
    port = 7000
    print("You need a port to connect to!!! Assuming 7000!!!")

  try:
    ssl = settings.setVariable("irc.ssl", settings.readConfig('IRC', 'ssl'))
  except:
    ssl = True
    print("Is this an ssl connection??? Assuming Yes!!!")

  try:
    nickname = settings.setVariable("irc.nickname", settings.readConfig('IRC', 'nickname'))
  except:
    nickname = "RoverDemo"
    print("You need a nickname to connect with!!! Assuming RoverDemo!!!")

  try:
    pw = settings.setVariable("irc.pw", settings.readConfig('IRC', 'pw'))
  except:
    print("A password was never specified!!! Assuming not needing one!!!")  

  try:
    loop()
  except:
    None
    #print("Cannot load IRC Robot!")

def loop():
  channel = "#bots"
  server = "irc.hackthissite.org"
  nickname = "reddity32323232"
 
  ##TODO TODO TODO
  #This file is a mess! I still have example code in here! It is not usable in this state!
  ##TODO TODO TODO

  irc = IRC()
  irc.connect(server, channel, nickname)

  while 1:
    text = irc.get_text()
    print(text)
 
    if "PRIVMSG" in text and channel in text and "hello" in text:
        irc.send(channel, "Hello!")

#################################################################################################
def send(self, chan, msg):
        self.irc.send("PRIVMSG " + chan + " " + msg + "n")

#################################################################################################
def connect(self, server, channel, botnick):
        #defines the socket
        print("connecting to:"+server)
        self.irc.connect((server, 6667))                                                         #connects to the server
        self.irc.send("USER " + botnick + " " + botnick +" " + botnick + " :This is a fun bot!n") #user authentication
        self.irc.send("NICK " + botnick + "n")               
        self.irc.send("JOIN " + channel + "n")        #join the chan

#################################################################################################
def handle(self, message):
  debug = settings.retrieveVariable("debug") # Should I turn this into a global or load it outside of a function?

  try:
    database.insertValues("irc", str(message))
  except:
    print("Cannot insert values into (irc) database!")

  text=message.irc.recv(2040)
 
  if text.find('PING') != -1:                      
    message.irc.send('PONG ' + text.split() [1] + 'rn') 

  if content_type == 'text':
    if debug:
      try:
        print("Message: %s" % message['text'])
      except UnicodeEncodeError:
        print("Message: %s" % message['text'].encode('latin-1', 'replace'))

    output = modules.allcommands("commands", message['text'])
    if output is not None:
      bot.sendMessage(chat_id, output)

  if debug:
    print() # Output a newline

  # So, I need to be able to figure out how to call the commands, 
  # parse their response, and then choose the appropriate method to send the data back!
  # For example, send photos with sendPhoto, 

#################################################################################################
if __name__ == "__main__":
  print("Please don't run me directly! I am module %s!\nMy purpose is to %s!" % (__module__, __purpose__))
