__author__ = 'SenorContento' #Me: Brandon Gomez
__module__ = 'debug'
__purpose__ = 'allow the owner to enable or disable debugging for everyone'

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
  import pyotp
except ImportError:
  print("ImportError! Cannot import pyotp (Python One Time Pad)!")

try:
  import settings
except ImportError:
  print("ImportError! Cannot import settings (This is a Rover library)!")

#################################################################################################
def init():
  global OTP

  try:
    OTP = settings.setVariable("otp", settings.readConfig('Admin', 'otp'))
  except:
    OTP = settings.setVariable("otp", pyotp.random_base32())
    print("Your temporary OTP Key (for the %s module) is: %s" % (__module__, OTP))
  #print("Debug: %s!" % execute("/debug 000000"))

#################################################################################################
def execute(command):
  debug = settings.retrieveVariable("debug")

  command = command.split(" ") # This allows me to split the user's message into an array!
  # So, design choice, do I split this before hand, or make every module do it? I do have performance I have to keep up!

  if command[0][1:].lower() == "debug": # Surely there must be a better way than nested if functions!!!
    if len(command) < 2:
      return("You need to provide the six digit code!")
    else:
      if len(command) < 3:
        if otp(command[1]):
          debug = not debug # Both "= not debug" and "~debug" result in inverting variables. Tilde converts it to -1 and 0 instead of false and true!
          settings.setVariable("debug", debug)
          return("The debugger has been set to " + str(debug).lower() + "!")
        else:
          return("Wrong OTP Code!")
      else:
        if otp(command[1]):
          if command[2].lower() == "true":
            debug = True
            settings.setVariable("debug", debug)
            return("The debugger has been set to " + str(debug).lower() + "!")
          if command[2].lower() == "false":
            debug = False
            settings.setVariable("debug", debug)
            return("The debugger has been set to " + str(debug).lower() + "!")
        else:
          return("Wrong OTP Code!")

#################################################################################################
def otp(code): # One Time Pad
  totp = pyotp.TOTP(OTP) # Grabs Key to Rover's OTP authentication!
  return totp.verify(code) # Verifies code against user input!

#################################################################################################
if __name__ == "__main__":
  print("Please don't run me directly! I am module %s!\nMy purpose is to %s!" % (__module__, __purpose__))
