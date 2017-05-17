import sqlite3

# http://pythoncentral.io/introduction-to-sqlite-in-python/

  try:
    DATABASE = parser.get('Database', 'File')
  except:
    DATABASE = "rover.sqlite"

  db = sqlite3.connect(DATABASE) #Not :memory:
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

  # Allows me to record messages for future reference!!!
  #cursor = db.cursor()
  #cursor.execute('''
  #  insert into telegram values (?,?,?,?,?,?,?,?,?)
  #  '''), 0, message['date'], message['text'], 
  #db.commit()

  db.close()
