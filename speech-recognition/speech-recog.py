from typing import List
import speech_recognition as sr
import argparse
from gtts import gTTS
import os
import playsound
import json
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
# Reset the log
logFile = open("latest.log", "w")
logFile.close()

# Function for both printing and adding to log.
def writeToLog(stringToLog:str, end:str='\n', endLine:bool=True, log_type:str='INFO'):
  logFile = open("latest.log", "a+")  # Open file
  logFile.write(f'[{log_type}] ' + stringToLog + end.rstrip('\n') + ('\n' if endLine else ''))
  print(stringToLog, end=end)
  logFile.close()

# Map for mob strings and their keywords
mobMap = None
try:
  with open("./data/keywords.json", 'r') as file:
    mobMap = json.load(file)
except:
  writeToLog("An error occurred while attempting to load keywords.json. Make sure the proper keywords.json file exists in the data folder!", type='ERR')
  exit(1)

if not mobMap:
  writeToLog("No data was found in keywords.json. Please ensure the file has data and try again.", type='ERR')
  exit(1)

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
  response = str(resp).replace(" ", "").lower()  # Reduces multiple words to one mish-mashed word -> strings like "village raid" contains "illager" if spaces are removed.
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