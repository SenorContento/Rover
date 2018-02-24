__author__ = 'SenorContento' #Me: Brandon Gomez
__module__ = 'help'
__purpose__ = 'suggest commands and other useful info to user'

#Imports
#################################################################################################
try:
  import settings
except ImportError:
  print("ImportError! Cannot import settings (This is a Rover library)!")

#################################################################################################
def init():
  None

#################################################################################################
def execute(command):
  debug = settings.retrieveVariable("debug") # Should I turn this into a global or load it outside of a function?

  command = command.split(" ") # This allows me to split the user's message into an array!
  # So, design choice, do I split this before hand, or make every module do it? I do have performance I have to keep up!

  if command[0][1:].lower() == "help":
    if debug:
      print("No Help Commands Available Yet!!!")

    return("Command Registration does not currently exist, so please visit https://rover.senorcontento.com/ for help!!!")

#################################################################################################
if __name__ == "__main__":
  print("Please don't run me directly! I am module %s!\nMy purpose is to %s!" % (__module__, __purpose__))
