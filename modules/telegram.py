import telepot
import telepot.loop

#################################################################################################
def telegram(token):
  global bot
  global uid

  try:
    token = parser.get('Telegram', 'token')
    token = settings.setVariable("telegram", settings.readConfig('Telegram', 'token'))
  except:
    print("You need a token to communicate with Telegram!!! Talk to @BotFather on Telegram!!!")
    sys.exit(1) # Eventually when I add more ways to communicate with Rover, then this won't be a hard requirement

  try:
    commands.initDatabase()
  except:
    print('Cannot initialize database ' + settings.DATABASE)
    print_exc()

  try:
    # Create access to bot
    bot = telepot.Bot(token)
    bot.setWebhook() # Should disable any webhook you have!
    botInfo = bot.getMe()
    print("Username: " + botInfo['username']) #Just putting print bot.getMe() will return JSON!
    print("Name: " + botInfo['first_name'])
    print("Robot's ID: " + str(botInfo['id']) + '\n') #str(Number) because you cannot directly combine int and string in Python!
    telepot.loop.MessageLoop(bot, commands.handle).run_as_thread() #run_forever()?
  except telepot.exception.TelepotException as e: #Why can I not catch this exception?
    print('Telegram Error! "%d: %s"' % (e.error_code, e.description))
  except:
    exClass = sys.exc_info()[0]
    exDesc = sys.exc_info()[1]
    print('"%s: %s"' % (exClass, exDesc))
