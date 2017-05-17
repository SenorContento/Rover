__author__ = 'SenorContento' #Me: Brandon Gomez

# When I wrote the program, I screwed up the concept of global variables (go figure by taking on python for the first time).
# So, I created this file as the solution
# https://stackoverflow.com/questions/13034496/using-global-variables-between-files

#Imports
#################################################################################################
from configparser import SafeConfigParser
import codecs

import os
import sys

import pyotp
import base64
import random

#Globals
#################################################################################################
# I don't believe I need these lines!!!
#################################################################################################

variables = {} # This is a dictionary! It can be used to create dynamic variables!

#ConfigParser
#################################################################################################
# Set Config File
SETTINGSFILE = 'rover.ini' # Maybe allow the command line (or function) to override this?

# Read Config File
parser = SafeConfigParser()

# Open the file with the correct encoding
with codecs.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), SETTINGSFILE), 'r', encoding='utf-8') as f:
  parser.readfp(f)
#################################################################################################

#Functions
#################################################################################################
def main():
  print('Please do not run this file directly! Instead, run rover.py')

#################################################################################################
def init():
  # Ensures Debug is a boolean
  try:
    #retrieveVariable("debug") # Not part of this code, just here for reference!
    DEBUG = parser.get('Admin', 'debug')
    if(DEBUG.lower() == "false"):
      DEBUG = False
    elif(DEBUG.lower() == "true"):
      DEBUG = True
    else: # Incase of malformed value
      DEBUG = True
  except: # Should I do KeyError or NoOptionError?
    DEBUG = False
  setVariable("debug", DEBUG)

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
if __name__ == "__main__":
  main()
