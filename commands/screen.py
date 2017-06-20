__author__ = 'SenorContento' #Me: Brandon Gomez
__module__ = 'screen'
__purpose__ = 'turn on and off my computer screen on command'

#Imports
#################################################################################################
try:
  import pyotp
except ImportError:
  print("ImportError! Cannot import pyotp (Python One Time Pad)!")

try:
  import settings
except ImportError:
  print("ImportError! Cannot import settings (This is a Rover library)!")

try:
  from subprocess import call
except ImportError:
  print("ImportError! Cannot import call from subprocess!")

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

  

  if debug:
    print("The screen is %s!" % True)

  if command[0][1:].lower() == "screen": # Surely there must be a better way than nested if functions!!!
    if len(command) < 2:
      return("You need to provide the six digit code!")
    else:
      if len(command) < 3:
        if otp(command[1]):
          # Flip screen on and off!
          return("The screen has been set to %s!" % False)
        else:
          return("Wrong OTP Code!")
      else:
        if otp(command[1]):
          if command[2].lower() == "true":
            call(["vcgencmd", "display_power", "1"]) # Turns Screen On!
            return("The screen has been turned on!")
          if command[2].lower() == "false":
            call(["vcgencmd", "display_power", "0"]) # Turns Screen Off!
            return("The screen has been turned off!")
        else:
          return("Wrong OTP Code!")

#################################################################################################
def otp(code): # One Time Pad
  totp = pyotp.TOTP(OTP) # Grabs Key to Rover's OTP authentication!
  return totp.verify(code) # Verifies code against user input!

#################################################################################################
if __name__ == "__main__":
  print("Please don't run me directly! I am module %s!\nMy purpose is to %s!" % (__module__, __purpose__))
