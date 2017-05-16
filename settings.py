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

#Functions
#################################################################################################
def main():
  print('Please do not run this file directly! Instead, run rover.py')

#################################################################################################
def init():
  # The globals work only if you define them as global within the function itself!
  global SETTINGSFILE
  global DATABASE
  global TOKEN
  global DEBUG
  global ADMIN
  global PASSWORD
  global OTPNAME # This is an example of why I need dynamic variables! If I turn the commands into modules, they need to be able to work without modifying this file!

  # Set Config File
  SETTINGSFILE = 'rover.ini' # Maybe allow the command line to override this?

  # Read Config File
  parser = SafeConfigParser()

  # Open the file with the correct encoding
  with codecs.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), SETTINGSFILE), 'r', encoding='utf-8') as f:
    parser.readfp(f)

  # Ensures Debug is a boolean
  try:
    DEBUG = parser.get('Admin', 'debug')

    if(DEBUG.lower() == "false"):
      DEBUG = False
    elif(DEBUG.lower() == "true"):
      DEBUG = True
    else: # Incase of malformed value
      DEBUG = True
  except: # Should I do KeyError or NoOptionError?
    DEBUG = False

  try:
    DATABASE = parser.get('Database', 'File')
  except:
    DATABASE = "rover.sqlite"

  try:
    TOKEN = parser.get('Telegram', 'token')
  except:
    print("You need a token to communicate with Telegram!!! Talk to @BotFather on Telegram!!!")
    sys.exit(1) # Eventually when I add more ways to communicate with Rover, then this won't be a hard requirement

  try:
    ADMIN = parser.get('Admin', 'otp')
  except:
    ADMIN = pyotp.random_base32()
    print("Your temporary OTP Key is: " + ADMIN)

  try:
    PASSWORD = parser.get('Admin', 'pw')
  except:
    PASSWORD = pyotp.random_base32() # Because I currently do not want to invest time in a password generator. Maybe later!
    print("Your temporary password is: " + PASSWORD)

  #random_bytes = os.urandom(16)
  #token = base64.b64encode(random_bytes).decode('utf-8')
  #print("RANDOM: " + str(random_bytes))

  try:
    PIN = parser.get('Admin', 'pin')
  except:
    PIN = random.randint(1000, 999999) # Because I currently do not want to invest time in a password generator. Maybe later!
    print("Your temporary pin is: " + str(PIN))

  try: # This name is used in generating the OTP URL for any authentication apps!!!
    OTPNAME = parser.get('OTP', 'name')
  except:
    OTPNAME = "Rover"

#################################################################################################
def retrieveGlobal(variable, value): # If I can figure out how to use dynamic globals, this can make the concept of globals more flexible for me!
  None

#################################################################################################
def setGlobal(variable): # If I can figure out how to use dynamic globals, this can make the concept of globals more flexible for me!
  None

#################################################################################################
def deleteGlobal(variable): # If I can figure out how to use dynamic globals, this can make the concept of globals more flexible for me!
  None

#################################################################################################
if __name__ == "__main__":
  main()
