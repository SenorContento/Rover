import telepot

  try:
    TOKEN = parser.get('Telegram', 'token')
  except:
    print("You need a token to communicate with Telegram!!! Talk to @BotFather on Telegram!!!")
    sys.exit(1) # Eventually when I add more ways to communicate with Rover, then this won't be a hard requirement
