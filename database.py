__author__ = 'SenorContento' #Me: Brandon Gomez
__named__ = 'the database'
__purpose__ = 'save data for Rover'

#Imports
#################################################################################################
try:
  import sqlite3
except ImportError:
  print("ImportError! Cannot import sqlite3!")

try:
  import datetime
except ImportError:
  print("ImportError! Cannot import datetime!")

try:
  import settings
except ImportError:
  print("ImportError! Cannot import settings (This is a Rover library)!")

#Database
#################################################################################################
try:
  DATABASE = settings.setVariable("sql", settings.readConfig('Database', 'file'))
except:
  DATABASE = settings.setVariable("sql", "rover.sqlite")

#Functions
#################################################################################################

def init():
  """ Initializes database, should have already been called by Rover, don't load yourself!!! """
  # http://pythoncentral.io/introduction-to-sqlite-in-python/
  # http://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html

  # Until you learn sqlite command line or get a graphical editor - https://sqliteonline.com/
  # LEARN HOW TO READ TABLES - http://www.sqlitetutorial.net/sqlite-select/

  global db
  global cursor

  db, cursor = connect()
  
  # BASIC DUMP TABLE
  # select column from table;
  # select * from telegram;

def connect():
    """ Loads database from config """
    db = sqlite3.connect(settings.retrieveVariable("sql"), check_same_thread=False) #Not :memory:
    # The check_same_thread=False is to get around the fact that Rover is multithreaded. This weakens security, but I will take the extra steps to make sure this doesn't happen.
    db.row_factory = sqlite3.Row
    cursor = db.cursor()

    return db, cursor

def addTable(table):
  """ Creates table for module or command!!! """
  cursor.execute('''CREATE TABLE if not exists ''' + table + ''' (rowID INTEGER PRIMARY KEY AUTOINCREMENT, date INTEGER, JSON TEXT)''')
  # TODO: The above code is super insecure. I need to figure out why sanitization results in syntax error and find the right syntax for dynamic tables.
  db.commit()

def insertValues(table, values):
  """ Inserts data into table! Values needs to be in JSON string format!!! """
  # This needs to be dynamic as I will eventually support more than just storing JSON!!!

  date = int(datetime.datetime.now().strftime("%s")) * 1000
  cursor.execute('''INSERT INTO ''' + table + ''' (rowID, date, JSON) VALUES(?,?,?)''', (None, date, values)) # Putting None allows for incremental rowIDs since cursor still requires some value even though it should not be needed.
  # TODO: The above code is super insecure. I need to figure out why sanitization results in syntax error and find the right syntax for dynamic tables.
  db.commit()

def exit():
  """ Commits and Closes Database """
  db.commit() # Should be completely unecessary, but good to make sure everything is committed!
  db.close() # Properly close the database

#################################################################################################
if __name__ == "__main__":
  print("Please don't run me directly! I am %s!\nMy purpose is to %s!" % (__named__, __purpose__))
