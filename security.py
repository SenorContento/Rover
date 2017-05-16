__author__ = 'SenorContento' #Me: Brandon Gomez

from configparser import SafeConfigParser
import codecs

import os
import sys

import settings

import pyotp

#Functions
#################################################################################################
def main():
  print('Please do not run this file directly! Instead, run rover.py')

#################################################################################################
def otp(code): # One Time Pad
  #global debug # Due to the way globals work, trying to add this in will make the code more complicated than it needs to be!!!
  totp = pyotp.TOTP(settings.ADMIN)

  #if debug:
  #  print("Current Base32: ", settings.ADMIN)
  #  print("Current OTP: ", totp.now())

  #if debug:
  #  print("True OTP: " + str(totp.verify(code)))

  return totp.verify(code)

#################################################################################################
def pw(password): # Password
  return password == settings.PASSWORD

#################################################################################################
def pin(pin): # Pin - Will be used in PBX if I can get that working
  return pin == settings.PIN

#################################################################################################
if __name__ == "__main__":
  main()
