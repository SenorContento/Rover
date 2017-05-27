__author__ = 'SenorContento' #Me: Brandon Gomez
__named__ = 'the settings file'
__purpose__ = 'handle variables for different modules load for Rover'

#Imports
#################################################################################################
try:
  import os
except ImportError:
  print("ImportError! Cannot import os!")

try:
  from configparser import SafeConfigParser
except ImportError:
  print("ImportError! Cannot import SafeConfigParser from configparser!")

try:
  import codecs
except ImportError:
  print("ImportError! Cannot import codecs!")

#Dictionaries
#################################################################################################
variables = {} # This is a dictionary! It can be used to create dynamic variables!

#ConfigParser - Just a note to future self, I stuck this here instead of init() because a lot of variables would not be accessible to the modules! 
#################################################################################################
# Set Config File
SETTINGSFILE = 'rover.ini' # Maybe allow the command line (or function) to override this?

# Objectify Config File
parser = SafeConfigParser()

# Open the file with the correct encoding
try:
  with codecs.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), SETTINGSFILE), 'r', encoding='utf-8') as f:
    parser.readfp(f)
except:
  print("Cannot open file %s!\n" % SETTINGSFILE)

#Functions
#################################################################################################
def init():
  # Ensures Debug is a boolean
  #retrieveVariable("debug") # Not part of this code, just here for reference!
  try:
    DEBUG = readConfig('Admin', 'debug')
    DEBUG = readBoolean(DEBUG, True)
    setVariable("debug", DEBUG)
  except: # Should I do KeyError or NoOptionError?
    DEBUG = False

#################################################################################################
def readConfig(section, key):
  return parser.get(section, key)

#################################################################################################
def writeConfig(section, key, value):
  None # This is currently not implemented!

#################################################################################################
def retrieveVariable(variable):
  return variables[variable]

#################################################################################################
def setVariable(variable, value):
  variables[variable] = value
  return variables[variable]

#################################################################################################
def deleteVariable(variable):
  del variables[variable]

#################################################################################################
def readBoolean(value, default):
  BOOL = False
  if(value.lower() == "false"):
    BOOL = False
  elif(value.lower() == "true"):
    BOOL = True
  else: # Incase of malformed value
    BOOL = default

  return BOOL

#################################################################################################
if __name__ == "__main__":
  print("Please don't run me directly! I am %s!\nMy purpose is to %s!" % (__named__, __purpose__))
