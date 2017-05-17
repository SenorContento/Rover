__author__ = 'SenorContento' #Me: Brandon Gomez
__module__ = 'pin'
__purpose__ = 'test whether or not the user can authenticate with a pin on a pbx machine'

#Imports
#################################################################################################
try:
  import os
except ImportError:
  print("ImportError! Cannot import os!")

try:
  import sys
except ImportError:
  print("ImportError! Cannot import sys!")

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

  #random_bytes = os.urandom(16)
  #token = base64.b64encode(random_bytes).decode('utf-8')
  #print("RANDOM: " + str(random_bytes))

  try:
    HASH = settings.setVariable("pin", settings.readConfig('Admin', 'pin'))
  except:
    hash256 = SHA256.new() # Creates new hashing algorithm object
    pin = settings.setVariable("pin", random.randint(1000, 999999)) # Because I currently do not want to invest time in a password generator. Maybe later!
    hash256.update(pin.encode('utf-8')) # Supplies text to hash
    HASH = hash256.digest() # Generates hash
    print("Your temporary pin is: " + pin)
    print("Your temporary pin's hash is: " + HASH)

#################################################################################################
def execute(command):
  command = command.split(" ") # This allows me to split the user's message into an array!
  # So, design choice, do I split this before hand, or make every module do it? I do have performance I have to keep up!

  #return("This command is designed to be used with a PBX machine! Please don't try executing this code!")

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
