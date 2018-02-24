__author__ = 'SenorContento' #Me: Brandon Gomez
__module__ = 'discord'
__purpose__ = 'communicate with the Discord server'

#Imports
#################################################################################################
try:
  import discord
except ImportError:
  print("ImportError! Cannot import discord!")

try:
  import asyncio
except ImportError:
  print("ImportError! Cannot import asyncio!")

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

client = discord.Client()

#Functions
#################################################################################################
def init():
  try:
    database.addTable("discord")
  except:
    print("Cannot create table in (discord) Database!")

  try:
    token = settings.setVariable("Discord.token", settings.readConfig('Discord', 'token'))
    #token = settings.setVariable("Discord.token", settings.readConfig('Discord', 'debugtoken'))
  except:
    print("You need a token to communicate with Discord!!! Go to https://discordapp.com/developers/applications/me!!!")

  loop = asyncio.get_event_loop()
  #asyncio.set_event_loop(loop)
  loop.run_until_complete(client.run(token)) # client.run is a blocking call!

#################################################################################################
@client.event
@asyncio.coroutine
def on_ready():
  try:
    oauth = settings.setVariable("Discord.oauth", settings.readConfig('Discord', 'oauth'))
    print("Your OAuth URL to register the bot on your server is %s" % oauth)
  except:
    try:
      print("Here is the URL to register the robot on the server! https://discordapp.com/oauth2/authorize?client_id=%s&scope=bot&permissions=0" % client.user.id)
    except:
      print("Cannot find CLIENT_ID without token! Here is the formula to register the robot on the server! https://discordapp.com/oauth2/authorize?client_id=CLIENT_ID&scope=bot&permissions=0")

  try:
    print("Username: %s" % client.user.name) #Just putting print bot.getMe() will return JSON!
    #print("Name: %s" % botInfo['first_name'])
    print("Robot's ID: %s\n" % client.user.id)
  except:
    None
    print("Cannot load Discord Robot!")

#################################################################################################
@client.event
@asyncio.coroutine
def on_message(message):
  debug = settings.retrieveVariable("debug") # Should I turn this into a global or load it outside of a function?
  
  try:
    database.insertValues("discord", str(message))
  except:
    print("Cannot insert values into (discord) database!")

  if debug:
    None

  content_type = 'text'
  if content_type == 'text':
    if debug:
      try:
        print("Message: %s" % message.content) #.startswith("test") - Maybe useful in increasing speed!
      except UnicodeEncodeError:
        print("Message: %s" % message.content.encode('latin-1', 'replace'))

    output = modules.allcommands("commands", message.content)
    if output is not None:
      yield from client.send_message(message.channel, output)

  if debug:
    print() # Output a newline

  # So, I need to be able to figure out how to call the commands, 
  # parse their response, and then choose the appropriate method to send the data back!
  # For example, send photos with sendPhoto, 

#################################################################################################
if __name__ == "__main__":
  print("Please don't run me directly! I am module %s!\nMy purpose is to %s!" % (__module__, __purpose__))