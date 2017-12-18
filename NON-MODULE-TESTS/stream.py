import pyotp
import qrcode
from io import BytesIO
from moviepy import editor as mpy

# This file is super short as I stupidly used "git reset --hard" without backing up my project files first.
# So, I used the part of the code I posted to "https://stackoverflow.com/questions/47773888/combine-audio-and-images-in-stream"
# and some code from the otp command (otp.py) to recreate this file as best as I could!

import numpy # So, I forgot this import on the question!

def make_image(text):
  img = qrcode.make(text)
  #output = BytesIO()
  output = "hello.png"
  img.save(output, format="PNG")
  #output.seek(0) # Going to the beginning of the file is required in order to have a photo to send to Telegram!
  return None

def make_frame(t):
  img = qrcode.make("Hello! The second is %s!" % t)
  return numpy.array(img.convert("RGB"))

make_image("Hello") # Based from otp.py

clip = mpy.VideoClip(make_frame, duration=10) # Could always set to 120
clip.write_gif("test.gif",fps=15)

gifclip = mpy.VideoFileClip("test.gif")
gifclip.set_duration(10).write_videofile("test.mp4",fps=15) # Same, 120
