import bandwidth
from PIL import Image, ImageDraw
from io import BytesIO
import json
from time import strftime
import datetime

user = 'u-REDACTED'
token = 't-REDACTED'
secret = 'REDACTED'

TO = "+1REDACTED"
FROM = "+1REDACTED"

SAVED_TIME = datetime.datetime.now()
TIME = SAVED_TIME.strftime("%Y-%m-%d %H:%M:%S")
NAME = ("Generated %s.png" % TIME)

WIDTH = 1920
HEIGHT = 1080

def demoImage():
    ''' Demo Image '''

    size = (WIDTH,HEIGHT) #width=1920,height=1080
    img = Image.new('RGBA', size) # The A puts in transparency!!!
    draw = ImageDraw.Draw(img) 
                                
    text_color = (49,64,253) # Royal Blue Plus Transparency - (65,105,225,0)
    text_pos = (10,10)
    text = "The current time is: %s!" % str(SAVED_TIME)
    
    draw.text(text_pos, text, fill=text_color)
    
    del draw
    
    output = BytesIO()
    img.save(output, format="PNG")
    output.seek(0) # Remember the problems with Telegram. It applies here too.

    return output

account_api = bandwidth.client('account', user, token, secret)
messaging_api = bandwidth.client('messaging', user, token, secret)

IMAGE = demoImage()
PHOTO = account_api.upload_media_file(NAME, content=IMAGE, content_type='image/png')
#PHOTO = None

#try:
#  print("Photo: %s" % PHOTO)
#except:
#  print("Photo: ")
#  print(PHOTO)

MEDIA = account_api.list_media_files()
MEDIAL = list(MEDIA)
#try:
#  print("Media: %s" % MEDIAL)
#except:
#  print("Media: ")
#  print(MEDIAL)

# GET URL
URL = None
for x in range(0,len(MEDIAL)):
  #print("Media: %s" % MEDIAL[x])
  data = json.dumps(MEDIAL[x])
  data = json.loads(data)
  
  MEDIA_NAME = data["media_name"]
  if MEDIA_NAME in NAME:
    URL = data["content"]
  print("Name: %s" % MEDIA_NAME)
  output, mime = account_api.download_media_file(MEDIA_NAME)
  binary = output.read() #.decode('utf-8')
  #print(str(binary))

  with open(MEDIA_NAME, "wb") as file: 
    file.write(binary)

  #account_api.delete_media_file(MEDIA_NAME)

message_id = messaging_api.send_message(from_ = FROM, to = TO, text = 'Hello World!!!', media=[URL])
print(message_id)

account_api.delete_media_file(NAME)

#while True:
#  messages = messaging_api.list_messages(to = TO)
#  mList = list(messages)
#  if len(mList) > 0:
    #print("Len: %s Messages: %s" % (len(mList),mList))
#    break


# FOR FUTURE REFERENCE

#my_message = api.get_message('m-messageId')
#print(my_message[state])

#call_list = call_api.list_calls(to = TO, size = 2)
#print(list(call_list))

#message_list = messaging_api.list_messages(to = TO)
#print(list(message_list))
