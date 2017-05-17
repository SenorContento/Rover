__author__ = 'SenorContento' #Me: Brandon Gomez
__module__ = 'password'
__purpose__ = 'test whether or not the user can authenticate with a password'

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

  try:
    HASH = settings.setVariable("pw", settings.readConfig('Admin', 'pw'))
  except:
    hash256 = SHA256.new() # Creates new hashing algorithm object
    password = settings.setVariable("pw", pyotp.random_base32()) # Because I currently do not want to invest time in a password generator. Maybe later!
    hash256.update(password.encode('utf-8')) # Supplies text to hash
    HASH = hash256.hexdigest() # Generates hash
    print("Your temporary password is: " + password)
    print("Your temporary password's hash is: " + HASH)

#################################################################################################
def execute(command):
  command = command.split(" ") # This allows me to split the user's message into an array!
  # So, design choice, do I split this before hand, or make every module do it? I do have performance I have to keep up!

  if command[0][1:].lower() == "password":
    if len(command) < 2:
      return("You need to supply the password as an argument!")
    else:
      return("Authenticated: %s" % pw(command[1]))

#################################################################################################
def pw(password): # Password
  hash256 = SHA256.new() # Creates new hashing algorithm object
  hash256.update(password.encode('utf-8')) # Supplies text to hash - I encode the password to utf-8 because giving an encoding is required!

  return hash256.hexdigest() == HASH

#################################################################################################
if __name__ == "__main__":
  print("Please don't run me directly! I am module %s!\nMy purpose is to %s!" % (__module__, __purpose__))
