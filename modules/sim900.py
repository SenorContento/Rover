__author__ = 'SenorContento' #Me: Brandon Gomez
__module__ = 'sim900'
__purpose__ = 'communicate with sim900 over UART (GPIO) on RPi3'

# TODO TODO TODO
# Create ability to use SMS, MMS, Calling, and Data.
# Their may be a subtype of calling involving a data connection
# Not all of this is testable without a working sim connection including all of these features
# * An example of not working is how I cannot set my voicemail with U.S. Mobile
# TODO TODO TODO

# NOTICE - Currently only SMS support will be added. More maybe coming soon!
# Also, MMS requires a data connection with APN settings, I cannot afford that just for experimentation
# right now, so I do not pay for data. If I get backers on Rover, then this could be a possibility.

#Imports
#################################################################################################
try:
  import serial
except ImportError:
  print("ImportError! Cannot import serial library (This is to connect to Sim900 over GPIO)!")

try:
  import binascii
except ImportError:
  print("ImportError! Cannot import binascii library (This is to convert between hex and binary)!")

try:
  import settings
except ImportError:
  print("ImportError! Cannot import settings (This is a Rover library)!")

try:
  import database
except ImportError:
  print("ImportError! Cannot import database (This is a Rover library)!")

try:
  import modules
except ImportError:
  print("ImportError! Cannot import modules (This is a Rover library)!")

#Functions
#################################################################################################
def init():
  try:
    database.addTable("sim900")
  except:
    print("Cannot create table in (sim900) Database!")

  try:
    device = settings.setVariable("sim900.device", settings.readConfig('Sim900', 'device'))
  except:
    print("You need a device to communicate with the modem!!! Defaulting to /dev/serial0!!!")
    device = settings.setVariable("sim900.device", "/dev/serial0")

  try:
    baud = int(settings.setVariable("sim900.baud", settings.readConfig('Sim900', 'baud')))
  except:
    print("You need a baudrate to know the timing of messages!!! Defaulting to 9600!!!")
    baud = int(settings.setVariable("sim900.baud", "9600"))

  try:
    timeout = int(settings.setVariable("sim900.timeout", settings.readConfig('Sim900', 'timeout')))
  except:
    print("You will want a timeout so Rover does not hang when not receiving messages!!! Defaulting to 1 second!!!")
    timeout = int(settings.setVariable("sim900.timeout", "1"))

    # From Python Docs
    # ----------------
    # timeout = None: wait forever / until requested number of bytes are received
    # timeout = 0: non-blocking mode, return immediately in any case, returning zero or more, up to the requested number of bytes
    # timeout = x: set timeout to x seconds (float allowed) returns immediately when the requested number of bytes are available, otherwise wait until the timeout expires and return all bytes that were received until then.

  ser = serial.Serial(port=device,baudrate=baud,timeout=timeout)
  setUPModem(ser)

  loop(ser)

  try:
    # Create access to bot
    #ser = serial.Serial(port='/dev/serial0',baudrate=9600,timeout=1)
    #setUPModem(ser)
    None # Remove when finished

    # TODO Run infinite loop here!
    #loop(ser)
  #except modem.exception.SomeException as e:
  #  print('Modem Error! "%d: %s"' % (e.error_code, e.description))
  except:
    None
    print("Cannot load modem!")

#################################################################################################
def loop(ser): # This is a blocking call, other modules after this will not load, needs to be fixed
  print("Begin - Loop")
  while(True):
    if(ser.inWaiting()):
      response = readResponse(ser)
      print("Response: %s" % response)
      
      if("CMTI" in str(response) and str(response).count(',' == 1)): # Example b'\r\n+CMTI: "SM",6\r\n'
        handle(grabMessage(response, ser), ser)
      elif("CMTI" in str(response) and str(response).count(',' > 1)):
        handle(grabMMS(response, ser), ser)

  print("End - Loop")

#################################################################################################
def writeCTRLZ():
  return(binascii.a2b_hex('1A')) # Substitute Character - ^z

#################################################################################################
def writeENTER():
  return(binascii.a2b_hex('0D')) # \r - CR (Carriage Return) (Do not use (0A or \n) LF (LineFeed or Newline))

#################################################################################################
def writeCommand(command, ser):
  finalCommand = command #bytes(command, 'utf-8')
  ser.write(finalCommand)
  return(finalCommand)

#################################################################################################
def readResponse(ser):
  bytesToRead = ser.inWaiting() # This does not work, why?
  rcv = ser.read(1000) # Read X number of bytes (or until end) # Could I use readline? Response should always end with \r\n
  return(rcv)

#################################################################################################
def sendCommand(command, ser):
  resultW = writeCommand(command, ser)
  rcv = readResponse(ser)
  
  if(True): #if(debug):
    print("########################################")
    print("Return Value Write Command: %s" % resultW)
    print("Return Value Read Command: %s" % rcv)
    print("########################################")

  return(rcv)

#################################################################################################
def toBin(command):
  rtn = bytes(command, 'utf-8') # Because converting \r or ^z to string does not work when converted back to bin
  return(rtn)

#################################################################################################
def setUPModem(ser):
  # FIGURE OUT HOW TO PROPERLY WAIT FOR RESPONSE
  print("Set UP Modem")
  sendCommand(toBin("AT") + writeENTER(), ser) # Check to see if result is OK
  sendCommand(toBin("AT+CMEE=2") + writeENTER(), ser) # Sets error messages to be human readable
  sendCommand(toBin("AT+CMGF=1") + writeENTER(), ser) # Sets text to SMS mode (Not MMS)
  sendCommand(toBin("AT+CLIP=1") + writeENTER(), ser) # Sets clip to display number calling sim900

  #sendCommand(toBin("AT+CMGS=\"+1REDACTED\"") + writeENTER(), ser) # Sets SMS reply Number
  #sendCommand(toBin("Starting Up!!!") + writeCTRLZ(), ser) # Types Message

#################################################################################################
def grabMMS(response, ser): # \r\n+CMTI: "SM",6\r\n
  # Can eventually be used to specify media type and/or pass on the raw URL to download the MMS

  # Although it is probably simpler and more logical to handle the MMS in house (in this module)
  # and not pass it off to a command module

  return("/handlemms %s" % "noSupport") # I currently do not support MMS and want to notify the user that tries to message Rover with MMS.

#################################################################################################
def grabMessage(response, ser): # \r\n+CMTI: "SM",6\r\n
  sResponse = response.decode("utf-8").strip() # Strips all newline characters # Don't use str(...). It will convert \r\n to literal ascii chars

  print("Original Response: %s, Stripped Response: %s" % (str(response), sResponse))

  if(sResponse.count(',' == 1): # This should never be false as I handle this in the notification handler loop().
    toss, number = sResponse.split(",", 1)

  rcv = sendCommand(toBin("AT+CMGR=%s" % number) + writeENTER(), ser) # Asks for message with number given by response
  
  print("Grabbed: %s" % rcv)

  sendCommand(toBin("AT+CMGD=%s" % number) + writeENTER(), ser) # Deletes message from sim card. Sim does not contain a lot of space, so this is necessary.

  return(rcv)

#################################################################################################
def handle(message, ser): # b'AT+CMGR=22\r\r\n+CMGR: "REC UNREAD","+1REDACTED","","18/02/06,18:59:04-20"\r\nCoolio\r\n\r\nOK\r\n'
  debug = settings.retrieveVariable("debug") # Should I turn this into a global or load it outside of a function?

  try:
    database.insertValues("sim900", str(message))
  except:
    print("Cannot insert values into (sim900) database!")

  parsedMessage = message.decode("utf-8").splitlines() # Decode the message before split, causes less headache
  print("Parsed Message: %s" % parsedMessage)

  unparsedNumber = parsedMessage[2] # +CMGR: "REC UNREAD","+1REDACTED","","18/02/06,18:59:04-20"
  message = parsedMessage[3] # The message should always be stored at position 3, if not I need to figure out how to properly parse it
  
  toss, number = unparsedNumber.split(",", 1) # Find a better way to parse the number
  number, toss = number.split(",", 1) # Find a better way to parse the number
  toss, number, toss1 = number.split("\"", 2) # Find a better way to parse the number

  print("Number: \"%s\"" % number)
  print("Pure Message: \"%s\"" % message)

  if(debug):
    print("Debug??? (Some Kind of Modem Values): %s" % debug)
    print("Could Print Phone #, etc...")

  if(debug):
    try:
      print("Message: %s" % message)
    except UnicodeEncodeError:
      print("Message: %s" % message.encode('latin-1', 'replace'))

  output = modules.allcommands("commands", message)
  if output is not None:
    print("Sim900 Reply: %s" % output)

    try:
      database.insertValues("sim900", "Reply: %s" % output)
    except:
      print("Cannot insert values into (sim900) database!")

    sendCommand(toBin("AT+CMGS=\"%s\"" % number) + writeENTER(), ser) # Sets SMS reply Number
    sendCommand(toBin(output) + writeCTRLZ(), ser) # Types Message
    #return(output)

  if(debug):
    print() # Output a newline

#################################################################################################
if __name__ == "__main__":
  print("Please don't run me directly! I am module %s!\nMy purpose is to %s!" % (__module__, __purpose__))
