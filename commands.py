__author__ = 'SenorContento' #Me: Brandon Gomez

###TODO TODO TODO
# I probably should just destroy the commands file entirely as I will be having multiple sources of input accessing the same command modules!
# It won't make sense to have a commands.py to handle Telegram requests when I already have a telegram.py!
###TODO TODO TODO

#Imports
#################################################################################################
from configparser import SafeConfigParser
import codecs

import os
import sys

import settings

#import json
#from PIL import Image

bot = telepot.Bot(settings.TOKEN) # I only need to initialize the bot once!

#Functions
#################################################################################################
def main():
  print('Please do not run this file directly! Instead, run rover.py')

#################################################################################################
def handle(message):
  flavor = telepot.flavor(message) # TODO: Do something with this when you add support for more than just plain text messages!!!

  data = json.loads(json.dumps(message)) #json.dumps converts python string to json string and json.loads parses json string
  uid = data['chat']['id']

  try:
    text = message['text'] #message['text'].upper()

    if text[0] == "/": # Should I allow a command anywhere in the message, or force it to be the first thing written in the message!!!
      command = text.split(" ")
      # This file is currently broken! I have made all commands into modules, I just haven't loaded and allowed execution yet!
  except: # Maybe check the message flavor first!!!
    None

  if debug:
    debug()

#################################################################################################
def debug():
  print("Message Flavor: " + str(flavor)) #chat, callback_query, inline_query, chosen_inline_result

  try:
    print("JSON: " + str(data))
  except UnicodeEncodeError:
    print("JSON: " + str(str(data).encode('latin-1', 'replace'))) #I only want the emojis to be replaced with question marks if the computer does not have the packages to support it. The emojis will still show up in Telegram!!!

  #bot = telepot.Bot(settings.TOKEN)
  try:
    bot.sendMessage(uid, "Hello " + data['from']['username'] + "! Here is your JSON: " + str(data))
  except UnicodeEncodeError:
    bot.sendMessage(uid, "Hello " + data['from']['username'] + "! Here is your JSON: " + str(str(data).encode('latin-1', 'replace')))
  except KeyError:
    #bot.sendMessage(uid, "Hello, it appears you have a KeyError! It most likely means Rover is on a Channel and cannot find out who sent the message!")
    print("Hello, it appears you have a KeyError! It most likely means Rover is on a Channel and cannot find out who sent the message!")
    bot.sendMessage(uid, "Hello " + data['chat']['title'] + "! Here is your JSON: " + str(str(data).encode('latin-1', 'replace')))

  try:
    bot.sendMessage(uid, "Here is your message \"" + data['text'] + "\"!")
  except UnicodeEncodeError:
    bot.sendMessage(uid, "Here is your message \"" + str(data['text'].encode('latin-1', 'replace')) + "\"!") #Same as with JSON!!!
  except KeyError:
    #bot.sendMessage(uid, "I am sorry, I cannot seem to grab the text, seems to be a KeyError!") #Same as with JSON!!!
    None

  try:
    print('Date: ' + str(data['date']))
  except KeyError as e:
    print('Commands.py/Date - KeyError: ' + e)

  try:
    print('Sender: ' + data['from']['username'] + ' - Message: ' + data['text'])
  except UnicodeEncodeError:
    print('Sender: ' + data['from']['username'] + ' - Message: ' + str(data['text'].encode('latin-1', 'replace')))
  except KeyError:
    print("A key is missing for Sender/Message! Most likely it is a message without text!!!")

  print() #Puts a newline!!!

#################################################################################################
if __name__ == "__main__":
  main()

