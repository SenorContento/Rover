__author__ = 'SenorContento' #Me: Brandon Gomez
__module__ = 'reddit'
__purpose__ = 'communicate with the Reddit server'

# PRAW Documentation = http://praw.readthedocs.io/en/latest/

#Imports
#################################################################################################
try:
  import praw
except ImportError:
  print("ImportError! Cannot import PRAW (A Reddit library)!")

try:
  import time
except ImportError:
  print("ImportError! Cannot import time!")

try:
  import settings
except ImportError:
  print("ImportError! Cannot import settings (This is a Rover library)!")

try:
  import database
except ImportError:
  print("ImportError! Cannot import database (This is a Rover library)!")

try:
  import modules
except ImportError:
  print("ImportError! Cannot import modules (This is a Rover library)!")

#Functions
#################################################################################################
def init():
  try:
    database.addTable("reddit")
  except:
    print("Cannot create table in (reddit) Database!")

  try:
    secret = settings.setVariable("reddit.secret", settings.readConfig('Reddit', 'secret'))
  except:
    print("You need a client secret! You may need to create a bot on https://www.reddit.com/prefs/apps/ to communicate with Reddit!!!")

  try:
    password = settings.setVariable("reddit.password", settings.readConfig('Reddit', 'password'))
  except:
   print("You need a password!")

  try:
    username = settings.setVariable("reddit.username", settings.readConfig('Reddit', 'username'))
  except:
   print("You need a username!")

  try:
    clientID = settings.setVariable("reddit.clientID", settings.readConfig('Reddit', 'clientID'))
  except:
   print("You need a clientID!")

  try:
    userAgent = settings.setVariable("reddit.userAgent", settings.readConfig('Reddit', 'userAgent'))
  except:
   print("You need a user agent! Just make one up!")

 # try:
    # Create access to bot
  global bot
  bot = praw.Reddit(client_id=clientID,
                      client_secret=secret,
                      password=password,
                      user_agent=userAgent,
                      username=username)
  loop()
  #except:
  #  None
    #print("Cannot load Reddit Robot!")

def loop():
  try:
    while True:
      pollSubreddit("DigitalRoverDev") #What we need to do is store this as an array in the config file!
      break; # Because let's please not spam! Just trying to get the code working!
      #sleep(1) # Let's not cross the rate limit in 5 seconds flat!
  #except RedditExceptionExample e:
    #print('Reddit Error! "%d: %s"' % (e.error_code, e.description))
  except:
    None
    #print("Poll Subreddit Exception! \"No Subreddit Determining Code Defined\"")

#################################################################################################
def pollSubreddit(subreddit):
  debug = settings.retrieveVariable("debug") # Should I turn this into a global or load it outside of a function?

  arbLimitPost = 10
  # You will want to set an arbitrary limit, unless you want to spend precious CPU time with going over a possible really long subreddit!
  # The cool thing with setting the limit with a variable is that with some framework, this robot can chose to change its own limit, say because it already has checked out a newer post, but needs to see an older post, which it does not have the id for.
  # If you wanted to remove the limit, just set it to None (e.g. limit=None)
  subreddit = bot.subreddit(subreddit)

  if debug:
    print("Subreddit: %s" % subreddit)
    print("----------------------------------------------------------------------------------------------------------------------------------------") # Need better way of formatting output!
    #print("Vars (Subreddit): %s" % vars(subreddit))
    #for moderator in subreddit.moderators: # Does not work. Also, no accurate info on mods when calling vars(...)
    #  print("Moderator: %s" % moderator)
    print()

  # TODO Reddit lies about the number of upvotes and downvotes (and votes in general)! It uses fuzzing to trick robots incase of shadowbanned!
  for submission in subreddit.hot(limit=arbLimitPost): #subreddit.hot(limit=1) # Set arbitrary limit
    if debug:
      print("Title (Submission): %s" % submission.title)
      print("Author (Submission): %s" % submission.author)
      print("Text (Submission): %s" % submission.selftext)
      print("Ups: %s, Downs: %s (Submission)" % (submission.ups, submission.downs))
      print("Score (Submission): %s" % submission.score)
      print("Comments (Submission): %s" % submission.num_comments)
      #print("Vars (Submission): %s" % vars(submission))
      print("ID (Submission): %s" % submission.id) #You can call for specific posts with the code reddit.submission(id=submission.id) or reddit.submission(id='3g1jfi')
      # The ID check method is great incase the robot already knows which post it needs to check either because it has visited the post before or a user gave it an ID or URL to check.
      print()
    reply = handle(submission.selftext) # Allows processing all submissions (but not the comments)
    replyTitle = handle(submission.title)
    # Noticed, I pulled out the whole submission and only left the body. The handle(...) function is generic and processes the raw data it is given.
    # It is meant for generic robot commands, not for Reddit specific features! Reddit specific features gets its own functions in this file.

    # Reply Stage
    if reply is not None:
      submission.reply(reply) # Reply to the current submission!!!
    if replyTitle is not None:
      submission.reply(replyTitle) # Reply to the current submission's title!!!
      #None # Disabled replying to submission (post)

    #-----------------------------------------------------------------------------------------------------------------------------------------------

    arbLimitComment = 100
    # Keep a separate limit on comment polls - Just set to None if you don't want a limit!
    # TODO - Figure out how to skip an arbitrary number of posts and comments to avoid buffer issue while still seeing all posts!

    submission.comments.replace_more(limit=arbLimitComment) # This loops through all comments
    for comment in submission.comments.list():
      if debug:
        print("Author (Comment): %s" % comment.author)
        print("Text (Comment): %s" % comment.body)
        print("Ups: %s, Downs: %s (Comment)" % (comment.ups, comment.downs))
        print("Score (Comment): %s" % comment.score)
        print("ID (Comment): %s" % comment.id)

      # Reply Stage
      reply = handle(comment.body)

      if reply is not None:
        comment.reply(reply) # Reply to the current comment!!!

#################################################################################################
def handle(message):
  #I can poll subreddits and DMs elsewhere and then process the messages themselves here!
  debug = settings.retrieveVariable("debug") # Should I turn this into a global or load it outside of a function?

  try:
    database.insertValues("reddit", str(message))
  except:
    print("Cannot insert values into (reddit) database!")

  #if debug:
  #  try:
  #    print("Message: %s" % message)
  #  except UnicodeEncodeError:
  #    print("Message: %s" % message.encode('latin-1', 'replace'))
  #  print()

  output = modules.allcommands("commands", message)
  
  #if output is not None: # Disabled because it needs to be handled by the calling code, otherwise it just hangs
  return(output)

#################################################################################################
if __name__ == "__main__":
  print("Please don't run me directly! I am module %s!\nMy purpose is to %s!" % (__module__, __purpose__))
