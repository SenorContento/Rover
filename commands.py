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

  try:
    print("JSON: " + str(data))
  except UnicodeEncodeError:
    print("JSON: " + str(str(data).encode('latin-1', 'replace'))) #I only want the emojis to be replaced with question marks if the computer does not have the packages to support it. The emojis will still show up in Telegram!!!

  bot = telepot.Bot(settings.TOKEN)
  uid = data['from']['id']

  try:
    bot.sendMessage(uid, "Hello " + data['from']['username'] + "! Here is your JSON: " + str(data)) #Sending back JSON, has errors with certain emojis \U0001f3db
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

  text = message['text'] #message['text'].upper()
  if text[0] == "/":
    command = text.split(" ")
    execute(command, uid)

  print() #Puts a newline!!!

  # Allows me to record messages for future reference!!!
  #cursor = db.cursor()
  #cursor.execute('''
  #  insert into telegram values (?,?,?,?,?,?,?,?,?)
  #  '''), 0, message['date'], message['text'], 
  #db.commit()

#################################################################################################
def execute(command, uid):
  bot = telepot.Bot(settings.TOKEN)
  if command[0][1:].lower() == "guess":
    bot.sendMessage(uid, "Guessing Game!!!")
    print("Guessing Game!!!")

#################################################################################################
if __name__ == "__main__":
  main()

