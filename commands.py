__author__ = 'SenorContento' #Me: Brandon Gomez

#Imports
#################################################################################################
import telepot
import sqlite3

from ConfigParser import SafeConfigParser
import codecs

import os
import sys

import settings

#Globals
#################################################################################################
#################################################################################################

#Functions
#################################################################################################
def main():
  print 'Please do not run this file directly! Instead, run rover.py'

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

  json = str(message) #This grabs the (pythonified) JSON from the message before we erase it!
  #message = message['text'] #message['text'].upper()
  #commands = message.split(" ")

  # Allows me to record messages for future reference!!!
  #cursor = db.cursor()
  #cursor.execute('''
  #  insert into telegram values (?,?,?,?,?,?,?,?,?)
  #  '''), 0, message['date'], message['text'], 
  #db.commit()

  try:
    print 'Message: ' + message['date']
  except:
    print 'Cannot get data'

  print 'JSON: ' + json

#################################################################################################
if __name__ == "__main__":
  main()

