__author__ = 'SenorContento' #Me: Brandon Gomez
__named__ = 'the starting file'
__purpose__ = 'start Rover'

#Imports
#################################################################################################
try:
  import time
except ImportError:
  print("ImportError! Cannot import time!")

try:
  import settings
except ImportError:
  print("ImportError! Cannot import settings (This is a Rover library)!")

try:
  import modules
except ImportError:
  print("ImportError! Cannot import modules (This is a Rover library)!")

#Functions
#################################################################################################
if __name__ == "__main__":
  settings.init()
  modules.loadfolder("commands") # Figure out what to do about Discord blocking!
  modules.loadfolder("modules")

  # Keep the program running.
  while 1:
    time.sleep(10)
