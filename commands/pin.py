__author__ = 'SenorContento' #Me: Brandon Gomez
__module__ = 'pin'
__purpose__ = 'test whether or not the user can authenticate with a pin on a pbx machine'

#Imports
#################################################################################################
try:
  import random
except ImportError:
  print("ImportError! Cannot import random!")

try:
  import settings
except ImportError:
  print("ImportError! Cannot import settings (This is a Rover library)!")

try:
  from Crypto.Hash import SHA256
except ImportError:
  print("ImportError! Cannot import SHA256 from Crypto.Hash! The package is pycrypto!")

#################################################################################################
def init():
  global HASH
  size = 6

  #random_bytes = os.urandom(16)
  #token = base64.b64encode(random_bytes).decode('utf-8')
  #print("RANDOM: " + str(random_bytes))

  try:
    HASH = settings.setVariable("pin", settings.readConfig('Admin', 'pin'))
  except:
    hash256 = SHA256.new() # Creates new hashing algorithm object
    pin = settings.setVariable("pin", str(random.randint(100000000000, 999999999999))[:size]) # I need a better way of generating a number of variable size
    hash256.update(pin.encode('utf-8')) # Supplies text to hash
    HASH = hash256.hexdigest() # Generates hash
    print("Your temporary pin (for the %s module) is: %s" % (__module__, pin))
    print("Your temporary pin's hash (for the %s module) is: %s" % (__module__, HASH))

#################################################################################################
def execute(command):
  command = command.split(" ") # This allows me to split the user's message into an array!
  # So, design choice, do I split this before hand, or make every module do it? I do have performance I have to keep up!

  if command[0][1:].lower() == "pin":
    if len(command) < 2:
      return("You need to supply the pin as an argument!")
    else:
      return("Authenticated: %s" % pin(command[1]))

#################################################################################################
def pin(pin): # Pin - Will be used in PBX if I can get that working
  hash256 = SHA256.new() # Creates new hashing algorithm object
  hash256.update(pin.encode('utf-8')) # Supplies text to hash - I encode the password to utf-8 because giving an encoding is required!

  return hash256.hexdigest() == HASH

#################################################################################################
if __name__ == "__main__":
  print("Please don't run me directly! I am module %s!\nMy purpose is to %s!" % (__module__, __purpose__))
