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

#Functions
#################################################################################################
def init():
  None

#################################################################################################
def telegram(token): # I haven't even messed with this yet, I am just trying to get the async imports working!
  global bot
  global uid

  try:
    token = parser.get('Telegram', 'token')
    token = settings.setVariable("telegram", settings.readConfig('Telegram', 'token'))
  except:
    print("You need a token to communicate with Telegram!!! Talk to @BotFather on Telegram!!!")
    sys.exit(1) # Eventually when I add more ways to communicate with Rover, then this won't be a hard requirement

  try:
    commands.initDatabase()
  except:
    print('Cannot initialize database ' + settings.DATABASE)
    print_exc()

  try:
    # Create access to bot
    bot = telepot.Bot(token)
    bot.setWebhook() # Should disable any webhook you have!
    botInfo = bot.getMe()
    print("Username: " + botInfo['username']) #Just putting print bot.getMe() will return JSON!
    print("Name: " + botInfo['first_name'])
    print("Robot's ID: " + str(botInfo['id']) + '\n') #str(Number) because you cannot directly combine int and string in Python!
    telepot.loop.MessageLoop(bot, commands.handle).run_as_thread() #run_forever()?
  except telepot.exception.TelepotException as e: #Why can I not catch this exception?
    print('Telegram Error! "%d: %s"' % (e.error_code, e.description))
  except:
    exClass = sys.exc_info()[0]
    exDesc = sys.exc_info()[1]
    print('"%s: %s"' % (exClass, exDesc))

#################################################################################################
if __name__ == "__main__":
  print("Please don't run me directly! I am module %s!\nMy purpose is to %s!" % (__module__, __purpose__))
