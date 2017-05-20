__author__ = 'SenorContento' #Me: Brandon Gomez
__module__ = 'start'
__purpose__ = 'let the user know any information needed to run the robot'

#Imports
#################################################################################################
None

#Functions
#################################################################################################
def init():
  None

#################################################################################################
def execute(command):
  command = command.split(" ") # This allows me to split the user's message into an array!
  # So, design choice, do I split this before hand, or make every module do it? I do have performance I have to keep up!

  if command[0][1:].lower() == "start":
    return("This robot currently can only support text messages! Support for photos, sound, documents and more is coming soon!")

#################################################################################################
if __name__ == "__main__":
  print("Please don't run me directly! I am module %s!\nMy purpose is to %s!" % (__module__, __purpose__))
