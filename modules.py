__author__ = 'SenorContento' #Me: Brandon Gomez
__named__ = 'the module loader'
__purpose__ = 'load modules for Rover'

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

#Functions
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
def runcommand(filepath, command):
    name,extension = os.path.splitext(os.path.split(filepath)[-1])

    if extension.lower() == '.py': # Checks if the extension of the module ends in .py (Scripted Python)
        module = imp.load_source(name, filepath)
    elif extension.lower() == '.pyc': # Checks if the extension of the module ends in .pyc (Compiled Python)
        module = imp.load_compiled(name, filepath)

    # Loads the function init
    init = 'execute'
    if hasattr(module, init):
        function = getattr(module, init)(command)

    return function

#################################################################################################
def allcommands(folder, command):
    debug = settings.retrieveVariable("debug") # Should I turn this into a global or load it outside of a function?
    files = os.listdir(folder)

    #TODO TODO TODO
    # I need to add a dictionary the the modules can register commands for so every module is not executed every time a command is run!
    # I want to support wildcard commands so modules that can interpret human speech can be created!
    # I also need to figure out how to get user sessions to work!
    #TODO TODO TODO

    for f in files:
      try:
        output = runcommand(os.path.join(folder, f), command)
        if debug:
          print("Module (%s) Output: %s" % (f, output))
        if output is not None: # This is a hack! I need to get the dictionary created and see if handling multiple commands with wildcards is possible!
          return output
      except UnboundLocalError: # I need quiet (except for the errors that are actually important)!
        None
      except: # Because not all files (or folders) in the commands folder are modules! Thanks __pycache__!
        from traceback import print_exc
        print_exc()

#################################################################################################
def exit(filepath):
    name,extension = os.path.splitext(os.path.split(filepath)[-1])

    if extension.lower() == '.py': # Checks if the extension of the module ends in .py (Scripted Python)
        module = imp.load_source(name, filepath)
    elif extension.lower() == '.pyc': # Checks if the extension of the module ends in .pyc (Compiled Python)
        module = imp.load_compiled(name, filepath)

    # Loads the function init
    init = 'exit'
    if hasattr(module, init):
        function = getattr(module, init)()

    return function

#################################################################################################
def exitfolder(folder):
    files = os.listdir(folder)

    #print("Files: %s" % files)
    #print("Number: %s" % len(files))

    for f in files:
      #print("File: %s" % f)
      try:
        exit(os.path.join(folder, f))
      except UnboundLocalError: # I need quiet (except for the errors that are actually important)!
        None
      except: # Because not all files (or folders) in the commands folder are modules! Thanks __pycache__!
        from traceback import print_exc
        print_exc()

#################################################################################################
if __name__ == "__main__":
  print("Please don't run me directly! I am %s!\nMy purpose is to %s!" % (__named__, __purpose__))

