__author__ = 'SenorContento' #Me: Brandon Gomez
__purpose__ = 'This is a test program designed to load modules for Rover!'

#Imports
#################################################################################################
try:
  import os
except ImportError:
  print("ImportError! Cannot import os!")

try:
  import imp
except ImportError:
  print("ImportError! Cannot import imp!")

try:
  import settings
except ImportError:
  print("ImportError! Cannot import settings (This is a Rover library)!")

#################################################################################################
def load(filepath):
    name,extension = os.path.splitext(os.path.split(filepath)[-1])

    if extension.lower() == '.py': # Checks if the extension of the module ends in .py (Scripted Python)
        module = imp.load_source(name, filepath)
    elif extension.lower() == '.pyc': # Checks if the extension of the module ends in .pyc (Compiled Python)
        module = imp.load_compiled(name, filepath)

    # Loads the function init
    init = 'init'
    if hasattr(module, init):
        function = getattr(module, init)()

    return function

#################################################################################################
def loadfolder(folder):
    files = os.listdir(folder)

    #print("Files: %s" % files)
    #print("Number: %s" % len(files))

    for f in files:
      #print("File: %s" % f)
      try:
        load(os.path.join(folder, f))
      except UnboundLocalError: # I need quiet (except for the errors that are actually important)!
        None
      except: # Because not all files (or folders) in the commands folder are modules! Thanks __pycache__!
        from traceback import print_exc
        print_exc()

#################################################################################################
if __name__ == "__main__":
  settings.init()
  loadfolder("commands")

