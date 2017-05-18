__author__ = 'SenorContento' #Me: Brandon Gomez

#Imports
#################################################################################################
try:
  import os
except ImportError:
  print("ImportError! Cannot import os!")

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
  modules.loadfolder("modules")
  modules.loadfolder("commands")

  # Keep the program running.
  while 1:
    time.sleep(10)
