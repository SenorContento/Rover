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
  # http://pythoncentral.io/introduction-to-sqlite-in-python/

  None
  
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

  # Allows me to record messages for future reference!!!
  #cursor = db.cursor()
  #cursor.execute('''
  #  insert into telegram values (?,?,?,?,?,?,?,?,?)
  #  '''), 0, message['date'], message['text'], 
  #db.commit()

def addTable(table):
  executecursor('''CREATE TABLE if not exists ''' + table + '''(rowID INTEGER PRIMARY KEY AUTOINCREMENT, date INTEGER, JSON TEXT)''')

def insertValues(table, values): # This needs to be dynamic as I will eventually support more than just storing JSON!!! I am only storing JSON just so I can have a working database at all, not because I want it to do this!
  date = int(datetime.datetime.now().strftime("%s")) * 1000
  executecursor('''INSERT INTO ''' + table + '''(rowID, date, JSON) VALUES(?,?)''', [(date, values)])

def executecursor(execute):
  db = sqlite3.connect(settings.retrieveVariable("sql")) #Not :memory:
  db.row_factory = sqlite3.Row
  cursor = db.cursor()

  cursor.execute(execute)
  db.close()

def executecursor(execute, values):
  # This is a mess, between the OperationalError and not being able to use cursor outside of the same function
  # https://stackoverflow.com/questions/20788403/inserting-to-sqlite-dynamically-with-python-3
  db = sqlite3.connect(settings.retrieveVariable("sql")) #Not :memory:
  db.row_factory = sqlite3.Row
  cursor = db.cursor()

  cursor.execute(execute, values)
  db.commit()
  db.close()

def exit():
  db.close()

#################################################################################################
if __name__ == "__main__":
  print("Please don't run me directly! I am %s!\nMy purpose is to %s!" % (__named__, __purpose__))
