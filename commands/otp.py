__author__ = 'SenorContento' #Me: Brandon Gomez
__module__ = 'otp'
__purpose__ = 'allow the user to generate and test OTP codes'

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

try:
  import qrcode
except ImportError:
  print("ImportError! Cannot import qrcode!")

try:
  from io import BytesIO
except ImportError:
  print("ImportError! Cannot import BytesIO from io!")

#################################################################################################
def init():
  global OTPNAME

  try: # This name is used in generating the OTP URL for any authentication apps!!!
    OTPNAME = settings.setVariable("otpname", settings.readConfig('OTP', 'name'))
  except:
    OTPNAME = settings.setVariable("otpname", "Rover")
  print("Execute: %s!" % execute("/otp qrcode"))

#################################################################################################
def execute(command):
  command = command.split(" ") # This allows me to split the user's message into an array!
  # So, design choice, do I split this before hand, or make every module do it? I do have performance I have to keep up!

  if command[0][1:].lower() == "otp":
    if len(command) < 3:
      if len(command) < 2: #if not command[1][1:]: # Checks if argument 2 is empty (or falsy)
        base32 = pyotp.random_base32()
        totp = pyotp.TOTP(base32)
      else:
        if command[1].lower() == "qrcode":
          base32 = pyotp.random_base32()
          totp = pyotp.TOTP(base32)

          try:
            img = qrcode.make(totp.provisioning_uri(OTPNAME)) # This creates the raw image (of the qr code)
            output = BytesIO() # This is a "file" written into memory
            img.save(output, format="PNG") # This is saving the raw image (of the qr code) into the "file" in memory
            output.seek(0) # Yeah, for real, this never occurred to me until it was pointed out to me on https://stackoverflow.com/questions/44012293/how-would-i-upload-a-bytesio-image-to-telegram-through-telepot-bot-sendphotouid # Going to the beginning of the file is required in order to have a photo to send to Telegram!
            bot.sendPhoto(uid, ('hello.png', output)) # This is sending the image file (in memory) to telegram!
          except:
            print_exc()

          output.close()
        else:
          base32 = command[1] # TODO: Probably not secure, should evaluate variable first
          totp = pyotp.TOTP(base32)
    else:
      if command[1].lower() == "qrcode":
        base32 = command[2]
        totp = pyotp.TOTP(base32)
        img = qrcode.make(totp.provisioning_uri(OTPNAME))
        output = BytesIO()
        img.save(output, format="PNG")
        output.seek(0) # Going to the beginning of the file is required in order to have a photo to send to Telegram!
        bot.sendPhoto(uid, output) # Allows sending photo of qr code back to user
        output.close()

    if debug:
      print("Provisioning URL: " + totp.provisioning_uri(OTPNAME)) # Just for messing around with OTP
    bot.sendMessage(uid, "Provisioning URL: " + totp.provisioning_uri(OTPNAME))

    if debug:
      print("Current Base32: ", base32) # Obviously debugging
      print("Current OTP: ", totp.now()) # Same
    bot.sendMessage(uid, "Current Base32: " + base32)
    bot.sendMessage(uid, "Current OTP: " + totp.now())

    if debug:
      # OTP verified for current time
      print("True OTP: " + str(totp.verify(totp.now()))) # => True

#################################################################################################
if __name__ == "__main__":
  print("Please don't run me directly! I am module %s!\nMy purpose is to %s!" % (__module__, __purpose__))
