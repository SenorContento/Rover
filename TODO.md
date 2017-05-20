###TODO TODO TODO
# Get database working so I can not only record messages, but also to have user sessions (for both multistep commands and remembering user preferences)
# Put commands into their own separate classes
# Change uid to chatid (or cid)
# Add ImportError (if you can) to help gracefully crash and instruct the user what packages to install!!!
# I may see about dynamic dns with the cloudflare api
# I am also considering linking the robot to external programs so I can use my Google Voice number with PBX software (as for real, who as a developer wouldn't want to control their robot or computer over the phone)
# I may split the commands into modules once I get the qrcode thing working so I can just enable and disable modules at will (and it will make developing modules more intuitive)
# Also, I need to be able to inform users if they are missing certain packages and how to find out/install the packages
# Maybe I will implement Hotbits (and Random.org) support for truly random numbers produced by radioactivity (and mostly random by atmospheric noise from Random.org)
# Add dictionary support (such as /define bliss)
# Add support for Rebrandly API
# Make a /sudo command so I can have Rover remember my uid (not cid) so I don't have to OTP every time I execute a command!
# Add a /kill (or /exit) command incase I need to shutoff my robot!
# Read RSS feeds
# Ping Speed Test
# Automatic Bot Creator (Via Chat APIs)
# TODO: Register commands via dictionary and support wildcard commands
# Maybe eventually support timing of commands and modules to test for inefficiencies
# Should I add an exit() function to modules (for cleanup, such as deleting variables from the dictionaries)?
# Add support for Discord server!
# Fix commands/guess.py (I never implemented the guessing game for lack of a database to store user sessions)!
# Fix commands/hash.py (I need to add support for multiple hashing algorithms that the user can specify to use)!
# Remove imports that I don't need! For example, do I need sys or os in every file?
###TODO TODO TODO

###Immediate Attention
# Fix database.py (There was no database to begin with, so you have to do this from scratch)
# Fix modules/telegram.py
#  * How should I send multiple messages from modules? Do I use an array?
#  * Fix commands/otp.py! I need to get Telegram working first!  
###Immediate Attention
