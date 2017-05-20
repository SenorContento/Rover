__author__ = 'SenorContento' #Me: Brandon Gomez
__module__ = 'hash'
__purpose__ = 'allow the user to hash data'

#Imports
#################################################################################################
try:
  from Crypto.Hash import SHA256
except ImportError:
  print("ImportError! Cannot import SHA256 from Crypto.Hash! The package is pycrypto!")

#################################################################################################
def init():
  #print("I am module %s!\nMy purpose is to %s!" % (__module__, __purpose__))
  #print("Hash: %s" % execute("/hash sha256 Cryptography Rules!!!"))
  None

#################################################################################################
def execute(command):
  command = command.split(" ") # This allows me to split the user's message into an array!
  # So, design choice, do I split this before hand, or make every module do it? I do have performance I have to keep up!

  if command[0][1:].lower() == "hash":
    if len(command) < 3:
      return("You need to supply a hash function and a message!!!")
    else:
      return("Hashing is not supported yet!!!")

#################################################################################################
if __name__ == "__main__":
  print("Please don't run me directly! I am module %s!\nMy purpose is to %s!" % (__module__, __purpose__))
