__author__ = 'SenorContento' #Me: Brandon Gomez

# When I wrote the program, I screwed up the concept of global variables (go figure by taking on python for the first time).
# So, I created this file as the solution
# https://stackoverflow.com/questions/13034496/using-global-variables-between-files

#Imports
#################################################################################################
import telepot
import sqlite3

from configparser import SafeConfigParser
import codecs

import os
import sys

#Globals
#################################################################################################
# I don't believe I need these lines!!!
#################################################################################################

#Functions
#################################################################################################
def main():
  print('Please do not run this file directly! Instead, run rover.py')

#################################################################################################
def init():
  # The globals work only if you define them as global within the function itself!
  global SETTINGSFILE
  global DATABASE
  global TOKEN

  # Set Config File
  SETTINGSFILE = 'rover.ini'

  # Read Config File
  parser = SafeConfigParser()

  # Open the file with the correct encoding
  with codecs.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), SETTINGSFILE), 'r', encoding='utf-8') as f:
    parser.readfp(f)

  DATABASE = parser.get('Database', 'File')
  TOKEN = parser.get('Telegram', 'token')

#################################################################################################
def retrieveGlobal(variable, value): # If I can figure out how to use dynamic globals, this can make the concept of globals more flexible for me!
  None

#################################################################################################
def setGlobal(variable): # If I can figure out how to use dynamic globals, this can make the concept of globals more flexible for me!
  None

#################################################################################################
def deleteGlobal(variable): # If I can figure out how to use dynamic globals, this can make the concept of globals more flexible for me!
  None

#################################################################################################
if __name__ == "__main__":
  main()
