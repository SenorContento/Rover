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

import json

#Globals
#################################################################################################
#################################################################################################

#Functions
#################################################################################################
def main():
  print('Please do not run this file directly! Instead, run rover.py')

#################################################################################################
def initDatabase():
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
  #cursor.execute('''
  #  SELECT name FROM sqlite_master
  #  WHERE type='table'
  #  ORDER BY name;
  #  ''')

  db.close()

#################################################################################################
def handle(message):
  # http://pythoncentral.io/introduction-to-sqlite-in-python/
  db = sqlite3.connect(settings.DATABASE) #Not :memory:
  db.row_factory = sqlite3.Row

  data = json.loads(json.dumps(message)) #json.dumps converts python string to json string and json.loads parses json string
  print("JSON: " + str(data))

  #message = message['text'] #message['text'].upper()
  #commands = message.split(" ")

  # Allows me to record messages for future reference!!!
  #cursor = db.cursor()
  #cursor.execute('''
  #  insert into telegram values (?,?,?,?,?,?,?,?,?)
  #  '''), 0, message['date'], message['text'], 
  #db.commit()

  bot = telepot.Bot(settings.TOKEN)
  uid = data['from']['id']
  bot.sendMessage(uid, "Hello " + data['from']['username'] + "! Here is your JSON: " + str(data))
  bot.sendMessage(uid, "Here is your message \"" + data['text'] + "\"!")

  try:
    print('Date: ' + data['date'])
  except:
    print('Cannot get data')

  print('Sender: ' + data['from']['username'] + ' - Message: ' + data['text'])

#################################################################################################
if __name__ == "__main__":
  main()

