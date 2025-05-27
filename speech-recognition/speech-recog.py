from typing import List
import speech_recognition as sr
import argparse
from gtts import gTTS
import os
import playsound
import json
import sys
from mc_connector import MCConnector

# Microphone selector
parser = argparse.ArgumentParser()
parser.add_argument("-m", "--Microphone", help="Select a microphone", action='store_true')
args = parser.parse_args()

# Speech recognizer
r = sr.Recognizer()  # Speech recognizer
r.energy_threshold = 300

# Log file for users to read on any errors
# ==================================================================================
import logging

# Configure logging
logging.basicConfig(
    filename="latest.log",
    filemode="w",
    format="[{levelname}] {message}",
    style="{",
    level=logging.INFO
)

# Function for both printing and adding to log.
def writeToLog(stringToLog:str, end:str='\n', logType:str='INFO'):
    log_level = getattr(logging, logType.upper(), logging.INFO)
    logging.log(log_level, stringToLog)
    print(stringToLog, end=end)

# Map for mob strings and their keywords
mobMap = None
try:
  with open("./data/keywords.json", 'r') as file:
    mobMap = json.load(file)
except FileNotFoundError:
  writeToLog("The file keywords.json was not found. Make sure the proper keywords.json file exists in the data folder!", logType='ERROR')
  sys.exit(1)
except json.JSONDecodeError:
  writeToLog("Failed to decode keywords.json. Ensure the file contains valid JSON data!", logType='ERROR')
  sys.exit(1)

if not mobMap:
  writeToLog("No data was found in keywords.json. Please ensure the file has data and try again.", logType='ERROR')
  sys.exit(1)

micNdx = None
if args.Microphone:
  for index, name in enumerate(sr.Microphone.list_microphone_names()):
    writeToLog(f"Microphone {name} found for 'Microphone(device_index = {index}')")

  micNdx = int(input("Enter the device index for the microphone you will be using: "))

mic = sr.Microphone(micNdx)
mcInstance = MCConnector(7777)  # Attempting to connect to Minecraft with the mod. The mod will also open this port on localhost.
writeToLog("Beginning speech recognition!")

def processResponse(response:str, cmdArray:List[str], ttsArray:List[str], containingArray:List[str]):
  # Iterate directly over mobMap items for efficiency and readability
  for mobToSpawn, mobData in mobMap.items():
    for keyword in mobData['keywords']:
      if keyword in response:
        cmdArray.append('spawn ' + mobToSpawn)
        ttsArray.append(mobData['tts_response'])
        containingArray.append(keyword)
        break


def playTTS(textToPlay:str):
  tts = gTTS(textToPlay, lang='en')
  fileName = "tts.mp3"
  tts.save(fileName)
  playsound.playsound(fileName)
  os.remove(fileName)  # Remove file when done


def getResponse(response:str):
  res = response
  response = str(res).replace(" ", "").lower()  # Reduces multiple words to one mish-mashed word -> strings like "village raid" contains "illager" if spaces are removed.
  response = str(response).replace("'", "")  # Removes any apostrophes from string

  mcCmds = []  # Commands to send to Minecraft
  ttsVoiceClips = []  # Strings to send to TTS
  contains = []  # Used to display what was found

  processResponse(response, mcCmds, ttsVoiceClips, contains)

  feedbackLine = res + (" (Contains " if contains else "")
  for word in contains:
    if word == contains[-1]:
      feedbackLine += word + ")"
    else:
      feedbackLine += word + ', '
  writeToLog(feedbackLine)
  return mcCmds, ttsVoiceClips


while True:
  try:
    with mic as src:
      r.adjust_for_ambient_noise(src)
      audio = r.listen(src)
      resp = r.recognize_google(audio)
      cmd, tts = getResponse(resp)

      for i in range(len(cmd)):
        mcInstance.stream(cmd[i])
        playTTS(tts[i])

  except sr.UnknownValueError:
    pass