__author__ = 'SenorContento' #Me: Brandon Gomez
__module__ = 'mms'
__purpose__ = 'handle MMS messages from Sim900'

#Imports
#################################################################################################
try:
  import settings
except ImportError:
  print("ImportError! Cannot import settings (This is a Rover library)!")

#################################################################################################
def init():
  try:
    NAME = settings.setVariable("admin.name", settings.readConfig('Admin', 'name'))
  except:
    NAME = settings.setVariable("admin.name", "Rover")

#################################################################################################
def execute(command):
  debug = settings.retrieveVariable("debug") # Should I turn this into a global or load it outside of a function?

  command = command.split(" ") # This allows me to split the user's message into an array!
  # So, design choice, do I split this before hand, or make every module do it? I do have performance I have to keep up!

  # "/handlemms %s" % "noSupport"
  if command[0][1:].lower() == "handlemms":
    if len(command) < 2:
      None
    else:
      if(command[1].lower() == "nosupport":)
        name = settings.retrieveVariable("admin.name")
        return("Sorry, but %s currently does not support MMS. Please just try normal SMS for now!" % name)

#################################################################################################
if __name__ == "__main__":
  print("Please don't run me directly! I am module %s!\nMy purpose is to %s!" % (__module__, __purpose__))
