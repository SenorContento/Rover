__author__ = 'SenorContento' #Me: Brandon Gomez
__module__ = 'weather'
__purpose__ = 'allow the user to learn about the weather'

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

#################################################################################################
def init():
  #print("I am module %s!\nMy purpose is to %s!" % (__module__, __purpose__))
  #print("Weather: %s" % execute("/weather nope"))
  None

#################################################################################################
def execute(command):
  command = command.split(" ") # This allows me to split the user's message into an array!
  # So, design choice, do I split this before hand, or make every module do it? I do have performance I have to keep up!

  if command[0][1:].lower() == "weather":
    if len(command) < 2:
      return("You need to supply the city (or coordinates) as an argument (or add a city as your preference)!!!")
    else:
      return("Weather is not supported yet!!!")

#################################################################################################
if __name__ == "__main__":
  print("Please don't run me directly! I am module %s!\nMy purpose is to %s!" % (__module__, __purpose__))
