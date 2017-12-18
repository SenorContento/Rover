__author__ = 'SenorContento' #Me: Brandon Gomez
__module__ = 'stream'
__purpose__ = 'communicate with the stream server'

# TODO TODO TODO
# I made this stream module "generic"!
# I do not know what program or library I will call to make this work and a module template is long overdue!
# TODO TODO TODO

#Imports
#################################################################################################
try:
  #import stream
except ImportError:
  print("ImportError! Cannot import stream library (This is to connect to stream)!")

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

#Functions
#################################################################################################
def init():
  try:
    database.addTable("stream")
  except:
    print("Cannot create table in (stream) Database!")

  try:
    token = settings.setVariable("stream.token", settings.readConfig('Stream', 'token'))
  except:
    print("You need a token to communicate with Stream server!!! Talk to Someone???!!!")

  try:
    # Create access to bot
    global bot
    bot = None # Some kind of Bot

    # TODO Run infinite loop here! loop()
  except stream.exception.SomeException as e:
    print('Stream Error! "%d: %s"' % (e.error_code, e.description))
  except:
    None
    #print("Cannot load Stream!")

#################################################################################################
def handle(message):
  debug = settings.retrieveVariable("debug") # Should I turn this into a global or load it outside of a function?

  try:
    database.insertValues("stream", str(message))
  except:
    print("Cannot insert values into (stream) database!")

  if debug:
    print("Debug??? (Some Kind of Stream Values): %s" % debug)

  if debug:
    try:
      print("Message: %s" % message)
    except UnicodeEncodeError:
      print("Message: %s" % message.encode('latin-1', 'replace'))

    output = modules.allcommands("commands", message)
    if output is not None:
      # Send Message!!! Stream Chat???

  if debug:
    print() # Output a newline

  # So, I need to be able to figure out how to call the commands, 
  # parse their response, and then choose the appropriate method to send the data back!
  # For example, send photos with sendPhoto, audio with sendAudio, text with sendText, etc...

#################################################################################################
if __name__ == "__main__":
  print("Please don't run me directly! I am module %s!\nMy purpose is to %s!" % (__module__, __purpose__))
