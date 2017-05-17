__author__ = 'SenorContento' #Me: Brandon Gomez
__module__ = 'guess'
__purpose__ = 'play a guessing game with the users of the bot'

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

#################################################################################################
def init():
  #print("I am module %s!\nMy purpose is to %s!" % (__module__, __purpose__))
  #print("Guess: %s!" % execute("/guess"))
  None

#################################################################################################
def execute(command):
  debug = settings.retrieveVariable("debug")

  command = command.split(" ") # This allows me to split the user's message into an array!
  # So, design choice, do I split this before hand, or make every module do it? I do have performance I have to keep up!

  if command[0][1:].lower() == "guess":
    if debug:
      print("Debug Guessing Game!!!")

    return("Guessing Game!!!")

#################################################################################################
if __name__ == "__main__":
  print("Please don't run me directly! I am module %s!\nMy purpose is to %s!" % (__module__, __purpose__))
