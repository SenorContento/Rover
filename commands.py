__author__ = 'SenorContento' #Me: Brandon Gomez

#Imports
#################################################################################################
import telepot
import sqlite3

from configparser import SafeConfigParser
import codecs

import os
import sys

import settings
import security

import json
import pyotp

import time

from traceback import print_exc

import qrcode
from io import StringIO, BytesIO

from PIL import Image

#Globals
#################################################################################################
#################################################################################################

#Functions
#################################################################################################
def main():
  print('Please do not run this file directly! Instead, run rover.py')

#################################################################################################
def initDatabase():
  ## DEBUGGER CHECKING
  try:
    global debug
    debug = settings.DEBUG
    if debug:
      print("DEBUG: true - Value: " + str(debug))
    else:
      print("DEBUG: false - Value: " + str(debug))
    print() # For Newline
  except:
    print("Cannot Test Debugger!!!")
    print_exc() # Prints Stacktrace
  ## END DEBUGGER CHECKING

  db = sqlite3.connect(settings.DATABASE) #Not :memory:
  db.row_factory = sqlite3.Row

  cursor = db.cursor()
  cursor.execute('''
    CREATE TABLE if not exists telegram(rowID INTEGER PRIMARY KEY, date INTEGER,
                       text TEXT, username TEXT, firstName TEXT, lastName TEXT, type TEXT, title TEXT, allMembersRAdministrators INTEGER
                       messageID INTEGER unique, ID INTEGER unique, updateID INTEGER unique,
                       JSON TEXT)
    ''')
  db.commit()
  
  # Can be used to list tables, just need to figure out how to read response to cursor!!!
  #try:
  #  if debug:
  #    cursor.execute('''
  #      SELECT name FROM sqlite_master
  #      WHERE type='table'
  #      ORDER BY name;
  #      ''')
  #except:
  #  print("Cannot List Tables!!!")
  #  print_exc()

  db.close()

#################################################################################################
def handle(message):
  flavor = telepot.flavor(message) # TODO: Do something with this when you add support for more than just plain text messages!!!
  if debug:
    print("Message Flavor: " + str(flavor))

  # http://pythoncentral.io/introduction-to-sqlite-in-python/
  db = sqlite3.connect(settings.DATABASE) #Not :memory:
  db.row_factory = sqlite3.Row
  # Allows me to record messages for future reference!!!
  #cursor = db.cursor()
  #cursor.execute('''
  #  insert into telegram values (?,?,?,?,?,?,?,?,?)
  #  '''), 0, message['date'], message['text'], 
  #db.commit()

  ###TODO TODO TODO
  # Get database working so I can not only record messages, but also to have user sessions (for both multistep commands and remembering user preferences)
  # Put commands into their own separate classes
  # Change uid to chatid (or cid)
  # Add ImportError (if you can) to help gracefully crash and instruct the user what packages to install!!!
  # I may see about dynamic dns with the cloudflare api
  # I am also considering linking the robot to external programs so I can use my Google Voice number with PBX software (as for real, who as a developer wouldn't want to control their robot or computer over the phone)
  # I may split the commands into modules once I get the qrcode thing working so I can just enable and disable modules at will (and it will make developing modules more intuitive)
  # Also, I need to be able to inform users if they are missing certain packages and how to find out/install the packages
  # Maybe I will implement Hotbits (and Random.org) support for truly random numbers produced by radioactivity (and mostly random by atmospheric noise from Random.org)
  ###TODO TODO TODO

  data = json.loads(json.dumps(message)) #json.dumps converts python string to json string and json.loads parses json string
  uid = data['from']['id']
  text = message['text'] #message['text'].upper()
  if text[0] == "/": # Should I allow a command anywhere in the message, or force it to be the first thing written in the message!!!
    command = text.split(" ")
    execute(command, uid)

  ## START DEBUG
  if debug:
    try:
      print("JSON: " + str(data))
    except UnicodeEncodeError:
      print("JSON: " + str(str(data).encode('latin-1', 'replace'))) #I only want the emojis to be replaced with question marks if the computer does not have the packages to support it. The emojis will still show up in Telegram!!!

    bot = telepot.Bot(settings.TOKEN)
    try:
      bot.sendMessage(uid, "Hello " + data['from']['username'] + "! Here is your JSON: " + str(data))
      bot.sendMessage(uid, "Here is your message \"" + data['text'] + "\"!")
    except UnicodeEncodeError:
      bot.sendMessage(uid, "Hello " + data['from']['username'] + "! Here is your JSON: " + str(str(data).encode('latin-1', 'replace')))
      bot.sendMessage(uid, "Here is your message \"" + str(data['text'].encode('latin-1', 'replace')) + "\"!") #Same as with JSON!!!

    try:
      print('Date: ' + str(data['date']))
    except KeyError as e:
      print('Commands.py/Date - KeyError: ' + e)

    try:
      print('Sender: ' + data['from']['username'] + ' - Message: ' + data['text'])
    except UnicodeEncodeError:
      print('Sender: ' + data['from']['username'] + ' - Message: ' + str(data['text'].encode('latin-1', 'replace')))

    print() #Puts a newline!!!
  ## END DEBUG

#################################################################################################
def execute(command, uid):
  ## TODO: I should probably split each command into a different class inside a folder called commands!!!
  global debug
  bot = telepot.Bot(settings.TOKEN)

  if command[0][1:].lower() == "debug": # Surely there must be a better way than nested if functions!!!
    if len(command) < 2:
      bot.sendMessage(uid, "You need to provide the six digit code!")
    else:
      if len(command) < 3:
        if security.otp(command[1]):
          debug = not debug # Both "= not debug" and "~debug" result in inverting variables. Tilde converts it to -1 and 0 instead of false and true!
          bot.sendMessage(uid, "The debugger has been set to " + str(debug) + "!")
        else:
          bot.sendMessage(uid, "Wrong OTP Code!")
      else:
        if security.otp(command[1]):
          if command[2].lower() == "true":
            debug = True
            bot.sendMessage(uid, "The debugger has been set to " + str(debug) + "!")
          if command[2].lower() == "false":
            debug = False
            bot.sendMessage(uid, "The debugger has been set to " + str(debug) + "!")
        else:
          bot.sendMessage(uid, "Wrong OTP Code!")

  if command[0][1:].lower() == "guess":
    bot.sendMessage(uid, "Guessing Game!!!")
    if debug:
      print("Guessing Game!!!")

  if command[0][1:].lower() == "otp":
    if len(command) < 3:
      if len(command) < 2: #if not command[1][1:]: # Checks if argument 2 is empty (or falsy)
        base32 = pyotp.random_base32()
        totp = pyotp.TOTP(base32)
      else:
        if command[1].lower() == "qrcode":
          base32 = pyotp.random_base32()
          totp = pyotp.TOTP(base32)
          img = qrcode.make(totp.provisioning_uri(settings.OTPNAME))
          output = BytesIO()
          img.save(output, format="PNG")

          #imgTwo = Image.open(output)
          #imgTwo.save("imgTwo.png", format="PNG") # So the qr code generates and saves just fine

          print("IMAGE: " + str(output)) # However, I cannot seem to get it to send the code back without some kind of error!
          bot.sendPhoto(uid, Image.frombytes('RGB',(400,400),output)) # Allows sending photo of qr code back to user
          output.close()
        else:
          base32 = command[1] # TODO: Probably not secure, should evaluate variable first
          totp = pyotp.TOTP(base32)
    else:
      if command[1].lower() == "qrcode":
        base32 = command[2]
        totp = pyotp.TOTP(base32)
        img = qrcode.make(totp.provisioning_uri(settings.OTPNAME))
        output = BytesIO()
        img.save(output, format="PNG")

        bot.sendPhoto(uid, output) # Allows sending photo of qr code back to user
        output.close()

    if debug:
      print("Provisioning URL: " + totp.provisioning_uri(settings.OTPNAME)) # Just for messing around with OTP
    bot.sendMessage(uid, "Provisioning URL: " + totp.provisioning_uri(settings.OTPNAME))

    if debug:
      print("Current Base32: ", base32) # Obviously debugging
      print("Current OTP: ", totp.now()) # Same
    bot.sendMessage(uid, "Current Base32: " + base32)
    bot.sendMessage(uid, "Current OTP: " + totp.now())

    if debug:
      # OTP verified for current time
      print("True OTP: " + str(totp.verify(totp.now()))) # => True

  if command[0][1:].lower() == "admin":
    if len(command) < 2:
      bot.sendMessage(uid, "You need to supply the six digit code as an argument!")
    else:
      bot.sendMessage(uid, "Authenticated: " + str(security.otp(command[1])))

  if command[0][1:].lower() == "password":
    if len(command) < 2:
      bot.sendMessage(uid, "You need to supply the password as an argument!")
    else:
      bot.sendMessage(uid, "Authenticated: " + str(security.pw(command[1])))

  if command[0][1:].lower() == "weather":
    if len(command) < 2:
      bot.sendMessage(uid, "You need to supply the city (or coordinates) as an argument (or add a city as your preference)!!!")
    else:
      bot.sendMessage(uid, "Weather is not supported yet!!!")

#################################################################################################
if __name__ == "__main__":
  main()

