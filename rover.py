__author__ = 'SenorContento' #Me: Brandon Gomez

#Imports
#################################################################################################
import telepot
import sqlite3

from configparser import SafeConfigParser
import codecs

import os
import sys

import time

import commands
import settings

import telepot.loop

#Globals
#################################################################################################
#################################################################################################

#Functions
#################################################################################################
def main():
  settings.init()
  telegram(settings.TOKEN)

#################################################################################################
def telegram(token):
  global bot
  global uid

  try:
    commands.initDatabase()
  except:
    #print 'Cannot initialize database ' + settings.DATABASE
    #print 'Chances are, it already exists!\n' #Add a check to make sure it doesn't already exist
    None # Because I don't want to deal with the error message right now!

  try:
    # Create access to bot
    bot = telepot.Bot(token)
    bot.setWebhook() # Should disable any webhook you have!
    botInfo = bot.getMe()
    print("Username: " + botInfo['username']) #Just putting print bot.getMe() will return JSON!
    print("Name: " + botInfo['first_name'])
    print("Robot's ID: " + str(botInfo['id']) + '\n') #str(Number) because you cannot directly combine int and string in Python!
    #print("Update: " + str(bot.getUpdates(offset=772199643))) #772199642 #772199641
    #bot.message_loop(commands.handle) # How do I switch over to telepot.loop.MessageLoop(bot, handler)? It keeps denying existance!
    telepot.loop.MessageLoop(bot, commands.handle).run_as_thread() #run_forever()? # I chose run_as_thread() because I am still in the stage of using Ctrl+C to end the program! It may take some time before I can get it to be like a service!
  except telepot.exception.TelepotException as e: #Why can I not catch this exception? Is it because I am using message_loop instead of handling the calling myself?
    print('Telegram Error! "%d: %s"' % (e.error_code, e.description))
  except:
    exClass = sys.exc_info()[0]
    exDesc = sys.exc_info()[1]
    print('"%s: %s"' % (exClass, exDesc))


  # Keep the program running.
  while 1:
    time.sleep(10)
#################################################################################################
if __name__ == "__main__":
  main()
