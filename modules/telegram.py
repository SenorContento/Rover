__author__ = 'SenorContento' #Me: Brandon Gomez
__module__ = 'telegram'
__purpose__ = 'communicate with the Telegram server'

#Imports
#################################################################################################
try:
  import telepot
except ImportError:
  print("ImportError! Cannot import telepot!")

try:
  import telepot.loop
except ImportError:
  print("ImportError! Cannot import telepot.loop!")

try:
  import asyncio
except ImportError:
  print("ImportError! Cannot import asyncio!")

# I seem to have some trouble importing the async part of telepot. The synchronous part works just fine!
try:
  import telepot.aio
except ImportError:
  print("ImportError! Cannot import telepot.aio!")

try:
  import telepot.aio.loop
except ImportError:
  print("ImportError! Cannot import telepot.aio.loop!")

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
    database.addTable("telegram")
  except:
    print("Cannot create table in (telegram) Database!")

  try:
    token = settings.setVariable("telegram.token", settings.readConfig('Telegram', 'token'))
    #token = settings.setVariable("telegram.token", settings.readConfig('Telegram', 'debugtoken'))
  except:
    print("You need a token to communicate with Telegram!!! Talk to @BotFather on Telegram!!!")

  try:
    # Create access to bot
    global bot
    bot = telepot.Bot(token)
    bot.setWebhook() # Should disable any webhook you have!
    botInfo = bot.getMe()

    print("Username: %s" % botInfo['username']) #Just putting print bot.getMe() will return JSON!
    print("Name: %s" % botInfo['first_name'])
    print("Robot's ID: %s\n" % botInfo['id'])

    telepot.loop.MessageLoop(bot, handle).run_as_thread() #run_forever()?
  except telepot.exception.TelepotException as e: #Why can I not catch this exception?
    print('Telegram Error! "%d: %s"' % (e.error_code, e.description))
  except:
    None
    #print("Cannot load Telegram Robot!")

#################################################################################################
def handle(message):
  debug = settings.retrieveVariable("debug") # Should I turn this into a global or load it outside of a function?
  content_type, chat_type, chat_id = telepot.glance(message) # This is quite literally a tuple with only these 3 values!

  database.insertValues("telegram", str(message))
  try:
    database.insertValues("telegram", str(message))
  except:
    print("Cannot insert values into (telegram) database!")

  if debug:
    print("Content Type: %s" % content_type)
    print("Chat Type: %s" % chat_type)
    print("Chat ID: %s" % chat_id)
    print("User ID: %s" % message['from']['id'])
    try:
      print("User Name: %s" % message['from']['username'])
    except:
      print("User Name is Not Available")
    try:
      print("First Name: %s" % message['from']['first_name'])
    except:
      print("First Name is Not Available")
    try:
      print("Last Name: %s" % message['from']['last_name'])
    except:
      print("Last Name is Not Available")

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
