###TODO TODO TODO
# Get database working so I can not only record messages, but also to have user sessions (for both multistep commands and remembering user preferences)
# Put commands into their own separate classes
# I may see about dynamic dns with the cloudflare api
# I am also considering linking the robot to external programs so I can use my Google Voice number with PBX software (as for real, who as a developer wouldn't want to control their robot or computer over the phone) - This may not happen if Google Voice quit allowing this :(
# Maybe I will implement Hotbits (and Random.org) support for truly random numbers produced by radioactivity (and mostly random by atmospheric noise from Random.org)
# Add dictionary support (such as /define bliss)
# Add support for Rebrandly API
# Make a /sudo command so I can have Rover remember my uid (not cid) so I don't have to OTP every time I execute a command!
# Add a /kill (or /exit) command incase I need to shutoff my robot!
# Read RSS feeds
# Ping Speed Test
# Automatic Bot Creator (Via Chat APIs)
# Register commands via dictionary and support wildcard commands
# Maybe eventually support timing of commands and modules to test for inefficiencies
# Should I add an exit() function to modules (for cleanup, such as deleting variables from the dictionaries)?
# Fix commands/guess.py (I never implemented the guessing game for lack of a database to store user sessions)!
# Fix commands/hash.py (I need to add support for multiple hashing algorithms that the user can specify to use)!
# Allow @ symbol to delimit command (i.e. /guess@RobotName)
# Add support to control Minecraft Client (and/or server) with python) - Should be easier with Raspberry Pi plugin. Let's see if I cannot do this on client side!
# http://docs.python-requests.org/en/master/user/quickstart/
# http://wiki.vg/Mojang_API
# Make support for Pocket Edition Minecraft (after PC version)
###TODO TODO TODO

###Immediate Attention
# Fix database.py (There was no database to begin with, so you have to do this from scratch)
# How should I send multiple messages from modules? Do I use an array? This also needs to support messages of different types!
###Immediate Attention
