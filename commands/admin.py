__author__ = 'SenorContento' #Me: Brandon Gomez
__module__ = 'admin'
__purpose__ = 'test whether or not the user can authenticate with OTP'

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

#Functions
#################################################################################################
def init():
  global OTP

  try:
    OTP = settings.setVariable("otp", settings.readConfig('Admin', 'otp'))
  except:
    OTP = settings.setVariable("otp", pyotp.random_base32())
    print("Your temporary OTP Key is: " + OTP)

  print("Admin: %s!" % execute("/admin 000000"))

#################################################################################################
def execute(command):
  command = command.split(" ") # This allows me to split the user's message into an array!
  # So, design choice, do I split this before hand, or make every module do it? I do have performance I have to keep up!

  if command[0][1:].lower() == "admin":
    if len(command) < 2:
      return("You need to supply the six digit code as an argument!")
    else:
      return("Authenticated: %s" % otp(command[1]))

#################################################################################################
def otp(code): # One Time Pad
  totp = pyotp.TOTP(OTP) # Grabs Key to Rover's OTP authentication!
  return totp.verify(code) # Verifies code against user input!

#################################################################################################
if __name__ == "__main__":
  print("Please don't run me directly! I am module %s!\nMy purpose is to %s!" % (__module__, __purpose__))
