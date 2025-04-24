from typing import List
import speech_recognition as sr
import argparse
from gtts import gTTS
import os
import playsound

# Microphone selector
parser = argparse.ArgumentParser()
parser.add_argument("-m", "--Microphone", help="Select a microphone", action='store_true')
args = parser.parse_args()

# Speech recognizer
r = sr.Recognizer()  # Speech recognizer
r.energy_threshold = 300

micNdx = None
if args.Microphone:
  for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print(f"Microphone {name} found for 'Microphone(device_index = {index}')")

  micNdx = int(input("Enter the device index for the microphone you will be using: "))

mic = sr.Microphone(micNdx)
print("Beginning speech recognition!")


def allocateToArrays(cmdString:str, ttsString:str, containString:str, cmdArray:List[str], ttsArray:List[str], containingArray:List[str]):
  cmdArray.append(cmdString)
  ttsArray.append(ttsString)
  containingArray.append(containString)


def playTTS(textToPlay:str):
  tts = gTTS(textToPlay, lang='en')
  fileName = "tts.mp3"
  tts.save(fileName)
  playsound.playsound(fileName)
  os.remove(fileName)  # Remove file when done


def getResponse(response:str):
  res = response
  response = str(resp).replace(" ", "").lower()  # Reduces multiple words to one mish-mashed word -> strings like "village raid" contains "illager" if spaces are removed.

  mcCmds = []  # Commands to send to Minecraft
  ttsVoiceClips = []  # Strings to send to TTS
  contains = []  # Used to display what was found

  # Finding strings in combined response and processing it.
  # Bee
  if "bee" in response:
    allocateToArrays("spawn bees", "Spawning angry bees, buzz buzz buzz.", "bee", mcCmds, ttsVoiceClips, contains)

  # Wolf
  if "dog" in response:
    allocateToArrays("spawn wolves", "Spawning angry wolves to steal your bones.", "dog", mcCmds, ttsVoiceClips, contains)
  elif "wolf" in response:  # Elif to avoid sending two TTS messages
    allocateToArrays("spawn wolves", "Spawning angry wolves to steal your bones.", "wolf", mcCmds, ttsVoiceClips, contains)

  # Iron Golem
  if "iron" in response:
    allocateToArrays("spawn iron golem", "Spawning an angry Iron Golem yeet you in the air.", "iron", mcCmds, ttsVoiceClips, contains)

  # Zombie
  if "zombie" in response:
    allocateToArrays("spawn zombies", "Spawning zombies to eat your brains.", "zombie", mcCmds, ttsVoiceClips, contains)
  elif "rot" in response:
    allocateToArrays("spawn zombies", "Spawning zombies to eat your brains.", "rot", mcCmds, ttsVoiceClips, contains)

  # Skeleton
  if "skeleton" in response:
    allocateToArrays("spawn skeletons", "Spawning skeletons, welcome to the bone zone.", "skeleton", mcCmds, ttsVoiceClips, contains)
  elif "bone" in response:
    allocateToArrays("spawn skeletons", "Spawning skeletons, welcome to the bone zone.", "bone", mcCmds, ttsVoiceClips, contains)

  if "awman" in response or "creeper" in response:
    mcCmds.append("Spawning Creepers to blow up your house.")
    if "awman" in response:
      contains.append("aw man")
    else:
      contains.append("creeper")
  if "spider" in response:
    mcCmds.append("Spawning spiders to climb your walls.")
    contains.append("spider")
  if "slime" in response:
    mcCmds.append("Spawning slimes to bounce on your head.")
    contains.append("slime")
  if "witch" in response:
    mcCmds.append("Spawning witches to cackle at you.")
    contains.append("witch")
  if "dark" in response or "warden" in response:
    mcCmds.append("Spawning Warden because you were too noisy.")
    if "dark" in response:
      contains.append("dark")
    else:
      contains.append("warden")
  if "silverfish" in response or "fish" in response or "silver" in response:
    mcCmds.append("Spawning silverfish to eat your stones.")
    if "silverfish" in response:
      contains.append("silverfish")
    elif "fish" in response:
      contains.append("fish")
    else:
      contains.append("silver")
  if "bed" in response or "sleep" in response or "phantom" in response:
    mcCmds.append("Spawning phantoms because you need some sleep.")
    if "bed" in response:
      contains.append("bed")
    elif "sleep" in response:
      contains.append("sleep")
    else:
      contains.append("phantom")
  if "illager" in response:
    mcCmds.append("Spawning Illagers to steal your emeralds.")
    contains.append("illager")
  if "ravager" in response:
    mcCmds.append("Spawning Ravagers to terrorize the village.")
    contains.append("ravager")
  if "pig" in response:
    mcCmds.append("Spawning angry Pigmen to steal your gold.")
    contains.append("pig")
  if "end" in response:
    mcCmds.append("Spawning angry Endermen to steal your blocks.")
    contains.append("end")
  if "skull" in response:
    mcCmds.append("Spawning Wither Skeletons to not drop Wither Skulls.")
    contains.append("skull")
  if "dragon" in response:
    mcCmds.append("Spawning Ender Dragon, good luck.")
    contains.append("dragon")
  if "wither" in response:
    mcCmds.append("Spawning Wither to shoot skulls at you.")
  if "tnt" in response:
    mcCmds.append("Spawning TNT, kaboom.")
    contains.append("tnt")

  print(res, end=" (Contains " if contains else "\n")
  for word in contains:
    if word == contains[-1]:
      print(word, end=")\n")
    else:
      print(word, end=", ")
  for cmd in ttsVoiceClips:
    playTTS(cmd)
  mcCmds.append(res)
  return mcCmds


while True:
  try:
    with mic as src:
      r.adjust_for_ambient_noise(src)
      audio = r.listen(src)
      resp = r.recognize_google(audio)
      cmd = getResponse(resp)
  except sr.UnknownValueError:
    pass