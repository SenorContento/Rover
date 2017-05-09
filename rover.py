__author__ = 'SenorContento' #Me: Brandon Gomez

#Imports
#################################################################################################
import telepot
import sqlite3

from ConfigParser import SafeConfigParser
import codecs

import os
import sys

import time

import commands
import settings

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
    botInfo = bot.getMe()
    print "Username: " + botInfo['username'] #Just putting print bot.getMe() will return JSON!
    print "Name: " + botInfo['first_name']
    print "Robot's ID: " + str(botInfo['id']) + '\n' #str(Number) because you cannot directly combine int and string in Python!
    #print "Update: " + str(bot.getUpdates(offset=772199643)) #772199642 #772199641
    bot.message_loop(commands.handle)
  except:
    print u'Cannot access Telegram. Please do /start'
    print u'Token: ' + token
    sys.exit(1)

  try: 
    message = bot.getUpdates()
    uid = u"%s" % message[0]['message']['from']['id']
    bot.sendMessage(uid, text=u"Start %s" % (os.path.basename(sys.argv[0])))
  except:
    None # I just added the NOP command to keep python happy with the fact there is no code for the exception!
    # print u"Error accessing Telegram, chances are you now need to send a message, not a command!"
    # Yeah, this is pointless when the program can now loop!

  # Keep the program running.
  while 1:
    time.sleep(10)
#################################################################################################
if __name__ == "__main__":
  main()
