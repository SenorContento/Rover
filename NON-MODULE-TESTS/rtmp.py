# Command Trying to Replicate in Python
# gst-launch-1.0 videotestsrc is-live=true ! autovideoconvert ! textoverlay text="Command Line" ! video/x-raw, width=1920,height=1080,framerate=30/1 ! x264enc bitrate=4000 tune=zerolatency key-int-max=60 option-string="keyint=60:min-keyint=60" ! queue ! flvmux name=mux ! rtmpsink location='rtmp://live.twitch.tv/app/STREAM_KEY' audiotestsrc is-live=true ! audioconvert ! audioresample ! audio/x-raw,rate=48000 ! voaacenc bitrate=96000 ! mux.

# ORIGINAL (UNEDITED) COMMAND - gst-launch-1.0 videotestsrc is-live=true ! videoconvert ! x264enc bitrate=1000 tune=zerolatency ! video/x-h264 ! h264parse ! video/x-h264 ! queue ! flvmux name=mux ! rtmpsink location='rtmp://live.twitch.tv/app/STREAM_KEY_HERE' audiotestsrc is-live=true ! audioconvert ! audioresample ! audio/x-raw,rate=48000 ! voaacenc bitrate=96000 ! audio/mpeg ! aacparse ! audio/mpeg, mpegversion=4 ! mux.

# ANOTHER WORKING COMMAND (For Youtube - It is because of audio stream) - gst-launch-1.0 videotestsrc is-live=1 ! video/x-raw,width=1920,height=1080,framerate=30/1 ! x264enc bitrate=1280 tune=zerolatency key-int-max=60 option-string="keyint=60:min-keyint=60" ! video/x-h264,profile=main ! queue ! mux. audiotestsrc is-live=1 wave=12 ! queue ! mux. flvmux streamable=1 name=mux ! rtmpsink location="rtmp://a.rtmp.youtube.com/live2/STREAM_KEY app=live2"

#STREAM_URL = "rtmp://live.twitch.tv/app/live_REDACTED?bandwidthtest=true" #?bandwidthtest=true

# Imports
import gi
import time
from gi.repository import GObject, Gst
import os

# OS Variables and Requirements
gi.require_version('Gst', '1.0')
os.environ["GST_DEBUG"] = "4" # Enable Debug

# Initialize GStreamer
Gst.init(None) # gst-launch-1.0 !
pipeline = Gst.Pipeline()

# Create Video Source (Video Test Source)
videosrc = Gst.ElementFactory.make("videotestsrc") # videotestsrc is-live=true !
#videosrc.set_property('pattern', 18)
videosrc.set_property('is-live', 1)
pipeline.add(videosrc)

# Convert Video (to x264enc?)
videoconvert = Gst.ElementFactory.make('autovideoconvert') # videoconvert
pipeline.add(videoconvert)

# (Setup) Overlay Text Over Video
#import datetime
textoverlay = Gst.ElementFactory.make("textoverlay", None)
#textoverlay.set_property("text","The current time is: %s!" % str(datetime.datetime.now()))
pipeline.add(textoverlay)

# Set Video Parameters
setHeight = Gst.Caps.from_string("video/x-raw, width=1920,height=1080,framerate=30/1")
setHeightFilter = Gst.ElementFactory.make("capsfilter", "setHeightFilter") 
setHeightFilter.set_property("caps", setHeight)
pipeline.add(setHeightFilter)

# Video Encoder (x264)
videoEncoder = Gst.ElementFactory.make("x264enc") # x264enc bitrate=1000 tune=zerolatency key-int-max=2 option-string="keyint=2:min-keyint=2"
videoEncoder.set_property('bitrate', 4000)
videoEncoder.set_property('tune', 'zerolatency')
videoEncoder.set_property('key-int-max', 60)
videoEncoder.set_property('option-string', "keyint=60:min-keyint=60")
pipeline.add(videoEncoder)

# Queue Data
queueRTMP = Gst.ElementFactory.make("queue") # queue
pipeline.add(queueRTMP)

# Convert to Mux
flvmux = Gst.ElementFactory.make("flvmux", "mux") # flvmux name=mux
pipeline.add(flvmux)

# Stream to RTMP Server
rtmpsink = Gst.ElementFactory.make("rtmpsink") # rtmpsink location='rtmp://live.twitch.tv/app/STREAM_KEY_HERE'
rtmpsink.set_property("location", STREAM_URL)
pipeline.add(rtmpsink)

#  audiotestsrc is-live=true ! audioconvert ! audioresample ! audio/x-raw,rate=48000 ! voaacenc bitrate=96000 ! audio/mpeg ! aacparse ! audio/mpeg, mpegversion=4 ! mux.

videosrc.link(videoconvert)
videoconvert.link(textoverlay)
textoverlay.link(setHeightFilter)
setHeightFilter.link(videoEncoder)
videoEncoder.link(queueRTMP)
queueRTMP.link(flvmux)
flvmux.link(rtmpsink)

# Audio +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
# rtmpsink location='rtmp://live.twitch.tv/app/STREAM_KEY' audiotestsrc is-live=true ! audioconvert ! audioresample ! audio/x-raw,rate=48000 ! voaacenc bitrate=96000 ! mux.

# Create Audio Source (Audio Test Source)
audiosrc = Gst.ElementFactory.make("audiotestsrc") # audiotestsrc is-live=true !
#videosrc.set_property('pattern', 18)
audiosrc.set_property('is-live', 1)
pipeline.add(audiosrc)

# Convert Audio (to AAC or MPEG?)
audioconvert = Gst.ElementFactory.make('audioconvert') # audioconvert
pipeline.add(audioconvert)

# Audio Resample???
audioresample = Gst.ElementFactory.make("audioresample") # audioresample
pipeline.add(audioresample)

# Set Audio Parameters (Something about Pads to link audio and video together, Check PDF)
setAudio = Gst.Caps.from_string("audio/x-raw,rate=48000")
setAudioFilter = Gst.ElementFactory.make("capsfilter", "setAudioFilter") 
setAudioFilter.set_property("caps", setAudio)
pipeline.add(setAudioFilter)

# Audio Encoder
audioEncoder = Gst.ElementFactory.make("voaacenc") # voaacenc bitrate=96000
audioEncoder.set_property('bitrate', 96000)
pipeline.add(audioEncoder)

audiosrc.link(audioconvert)
audioconvert.link(audioresample)
audioresample.link(setAudioFilter)
setAudioFilter.link(audioEncoder)
audioEncoder.link(flvmux)

#Gst.Element.link(rtmpsink, sink_audio)

pipeline.set_state(Gst.State.PLAYING)

import datetime
while True:
  textoverlay.set_property("text","The current time is: %s!" % str(datetime.datetime.now()))

#time.sleep(9999)
