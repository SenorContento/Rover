__author__ = 'SenorContento' #Me: Brandon Gomez
__module__ = 'phone'
__purpose__ = 'communicate via text message (and maybe eventually calling)'


#Imports
#################################################################################################
try:
  import bandwidth
except ImportError:
  print("ImportError! Cannot import bandwidth library (Use pip3 with bandwidth-sdk)!")

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
    database.addTable("bandwidth")
  except:
    print("Cannot create table in (bandwidth) Database!")

  try:
    user = settings.setVariable("Bandwidth.user", settings.readConfig('Bandwidth', 'user'))
  except:
    print("You need a user id to communicate with Bandwidth server!!! You can find it at https://app.bandwidth.com/account/profile!!!")

  try:
    token = settings.setVariable("Bandwidth.token", settings.readConfig('Bandwidth', 'token'))
  except:
    print("You need a token to communicate with Bandwidth server!!! You can find it at https://app.bandwidth.com/account/profile!!!")

  try:
    secret = settings.setVariable("Bandwidth.secret", settings.readConfig('Bandwidth', 'secret'))
  except:
    print("You need a secret to communicate with Bandwidth server!!! You can find it at https://app.bandwidth.com/account/profile!!!")

  try:
    number = settings.setVariable("Bandwidth.number", settings.readConfig('Bandwidth', 'number'))
  except:
    print("You need a phone number to communicate with Bandwidth server!!! You can find it at https://app.bandwidth.com/numbers/order!!!")

  # APIs
  account_api = bandwidth.client('account', user, token, secret)
  messaging_api = bandwidth.client('messaging', user, token, secret)
  #voice_api = bandwidth.client('voice', user, token, secret)

  try:
    while True:
      messages = messaging_api.list_messages(to = number)
      mList = list(messages)
      if len(mList) > 0:
        handle(mList)

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

#################################################################################################
if __name__ == "__main__":
  print("Please don't run me directly! I am module %s!\nMy purpose is to %s!" % (__module__, __purpose__))
