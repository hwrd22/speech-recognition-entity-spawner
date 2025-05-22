from typing import List
import speech_recognition as sr
import argparse
from gtts import gTTS
import os
import playsound
from mc_connector import MCConnector

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
mcInstance = MCConnector(7777)  # Attempting to connect to Minecraft with the mod. The mod will also open this port on localhost.
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
    allocateToArrays("spawn bee", "Spawning angry bees, buzz buzz buzz.", "bee", mcCmds, ttsVoiceClips, contains)

  # Wolf
  if "dog" in response:
    allocateToArrays("spawn wolf", "Spawning angry wolves to steal your bones.", "dog", mcCmds, ttsVoiceClips, contains)
  elif "wolf" in response:  # Elif to avoid sending two TTS messages
    allocateToArrays("spawn wolf", "Spawning angry wolves to steal your bones.", "wolf", mcCmds, ttsVoiceClips, contains)
  
  # Polar Bear
  if "bear" in response:
    allocateToArrays("spawn polar_bear", "Spawning angry polar bears because you insulted their baby.", "bear", mcCmds, ttsVoiceClips, contains)

  # Iron Golem
  if "iron" in response:
    allocateToArrays("spawn iron_golem", "Spawning an angry Iron Golem to yeet you in the air.", "iron", mcCmds, ttsVoiceClips, contains)

  # Zombie
  if "zombie" in response:
    allocateToArrays("spawn zombie", "Spawning zombies to eat your brains.", "zombie", mcCmds, ttsVoiceClips, contains)
  elif "rot" in response:
    allocateToArrays("spawn zombie", "Spawning zombies to eat your brains.", "rot", mcCmds, ttsVoiceClips, contains)

  # Skeleton
  if "skeleton" in response:
    allocateToArrays("spawn skeleton", "Spawning skeletons, welcome to the bone zone.", "skeleton", mcCmds, ttsVoiceClips, contains)
  elif "bone" in response:
    allocateToArrays("spawn skeleton", "Spawning skeletons, welcome to the bone zone.", "bone", mcCmds, ttsVoiceClips, contains)

  # Creeper
  if "creeper" in response:
    allocateToArrays("spawn creeper", "Spawning Creepers to blow up your house.", "creeper", mcCmds, ttsVoiceClips, contains)
  elif "cat" in response:  # Cat being associated with Creepers in some way, not rigged at all
    allocateToArrays("spawn creeper", "Spawning Creepers to blow up your house.", "cat", mcCmds, ttsVoiceClips, contains)

  # Spider
  if "spider" in response:
    allocateToArrays("spawn spider", "Spawning spiders to climb your walls.", "spider", mcCmds, ttsVoiceClips, contains)
  elif "bug" in response:  # Generally the most common "bug" encountered in the game
    allocateToArrays("spawn spider", "Spawning spiders to climb your walls.", "bug", mcCmds, ttsVoiceClips, contains)

  # Witch
  if "witch" in response:
    allocateToArrays("spawn witch", "Spawning witches to cackle at you.", "witch", mcCmds, ttsVoiceClips, contains)

  # Silverfish
  if "silverfish" in response:
    allocateToArrays("spawn silverfish", "Spawning silverfish to eat your stones.", "silverfish", mcCmds, ttsVoiceClips, contains)
  elif "silver" in response:
    allocateToArrays("spawn silverfish", "Spawning silverfish to eat your stones.", "silver", mcCmds, ttsVoiceClips, contains)
  elif "fish" in response:
    allocateToArrays("spawn silverfish", "Spawning silverfish to eat your stones.", "fish", mcCmds, ttsVoiceClips, contains)

  # Phantom
  if "bed" in response:  # Relates to phantoms spawning if the player hasn't slept
    allocateToArrays("spawn phantom", "Spawning phantoms because you need some sleep.", "bed", mcCmds, ttsVoiceClips, contains)
  elif "sleep" in response:  # Ditto
    allocateToArrays("spawn phantom", "Spawning phantoms because you need some sleep.", "sleep", mcCmds, ttsVoiceClips, contains)
  elif "phantom" in response:
    allocateToArrays("spawn phantom", "Spawning phantoms because you need some sleep.", "phantom", mcCmds, ttsVoiceClips, contains)

  # Enderman
  if "end" in response:
    allocateToArrays("spawn enderman", "Spawning angry Endermen to steal your blocks.", "end", mcCmds, ttsVoiceClips, contains)
  
  # Illager (Will be Pillager in Minecraft)
  if "illager" in response:
    allocateToArrays("spawn pillager", "Spawning Illagers to steal your emeralds.", "illager", mcCmds, ttsVoiceClips, contains)
  elif "raid" in response:  # Pillagers are associated with raids
    allocateToArrays("spawn pillager", "Spawning Illagers to steal your emeralds.", "raid", mcCmds, ttsVoiceClips, contains)
  
  # Ravager
  if "ravager" in response:
    allocateToArrays("spawn ravager", "Spawning a Ravager to terrorize the village.", "ravager", mcCmds, ttsVoiceClips, contains)

  # Slime
  if "slime" in response:
    allocateToArrays("spawn slime", "Spawning slimes to bounce on your head.", "slime", mcCmds, ttsVoiceClips, contains)
  
  # Breeze
  if "breeze" in response:
    allocateToArrays("spawn breeze", "Spawning Breezes to blow you away.", "breeze", mcCmds, ttsVoiceClips, contains)
  elif "wind" in response:
    allocateToArrays("spawn breeze", "Spawning Breezes to blow you away.", "wind", mcCmds, ttsVoiceClips, contains)
  
  # Guardian
  if "guard" in response:
    allocateToArrays("spawn guardian", "Spawning Guardians to go pew pew at you.", "guard", mcCmds, ttsVoiceClips, contains)
  elif "sea" in response:  # Guardians are found in ocean monuments
    allocateToArrays("spawn guardian", "Spawning Guardians to go pew pew at you.", "sea", mcCmds, ttsVoiceClips, contains)
  elif "ocean" in response:  # Ditto
    allocateToArrays("spawn guardian", "Spawning Guardians to go pew pew at you.", "ocean", mcCmds, ttsVoiceClips, contains)

  # Blaze
  if "blaze" in response:
    allocateToArrays("spawn blaze", "Spawning Blazes to set you on fire.", "blaze", mcCmds, ttsVoiceClips, contains)
  elif "fire" in response:  # Blazes fire fireballs to players
    allocateToArrays("spawn blaze", "Spawning Blazes to set you on fire.", "fire", mcCmds, ttsVoiceClips, contains)

  # Piglin
  if "pig" in response:
    allocateToArrays("spawn piglin", "Spawning angry Piglins to steal your gold.", "pig", mcCmds, ttsVoiceClips, contains)

  # Piglin Brute
  if "brute" in response:
    allocateToArrays("spawn piglin_brute", "Spawning a Piglin Brute to steal your gold with gold.", "brute", mcCmds, ttsVoiceClips, contains)
  
  # Ghast
  if "ghast" in response:
    allocateToArrays("spawn ghast", "Spawning Ghasts to wail at you.", "ghast", mcCmds, ttsVoiceClips, contains)
  elif "ghost" in response:  # Ghasts are sometimes compared with ghosts/souls
    allocateToArrays("spawn ghast", "Spawning Ghasts to wail at you.", "ghost", mcCmds, ttsVoiceClips, contains)
  elif "soul" in response:  # Ditto
    allocateToArrays("spawn ghast", "Spawning Ghasts to wail at you.", "soul", mcCmds, ttsVoiceClips, contains)

  # Wither Skeleton
  if "skull" in response:  # Wither skeletons drop Wither Skulls, an important item in Minecraft
    allocateToArrays("spawn wither_skeleton", "Spawning Wither Skeletons to not drop Wither Skulls.", "skull", mcCmds, ttsVoiceClips, contains)
  
  # Hoglin
  if "hog" in response:
    allocateToArrays("spawn hoglin", "Spawning Hoglins to headbutt you.", "hog", mcCmds, ttsVoiceClips, contains)
  
  # Magma Cube
  if "magma" in response:
    allocateToArrays("spawn magma_cube", "Spawning Magma Cubes to bounce with fire.", "magma", mcCmds, ttsVoiceClips, contains)
  elif "lava" in response:
    allocateToArrays("spawn magma_cube", "Spawning Magma Cubes to bounce with fire.", "lava", mcCmds, ttsVoiceClips, contains)

  # Endermite
  if "mite" in response:
    allocateToArrays("spawn endermite", "Spawning Endermites because you forgot they existed.", "mite", mcCmds, ttsVoiceClips, contains)
  elif "pearl" in response:  # Since they spawn from ender pearls
    allocateToArrays("spawn endermite", "Spawning Endermites because you forgot they existed.", "pearl", mcCmds, ttsVoiceClips, contains)

  # Shulker
  if "shulker" in response:
    allocateToArrays("spawn shulker", "Spawning Shulkers to lift you up into the air.", "shulker", mcCmds, ttsVoiceClips, contains)
  elif "chest" in response:  # Will be using all storage blocks for this mob
    allocateToArrays("spawn shulker", "Spawning Shulkers to lift you up into the air.", "chest", mcCmds, ttsVoiceClips, contains)
  elif "box" in response:  # It IS called a Shulker Box so
    allocateToArrays("spawn shulker", "Spawning Shulkers to lift you up into the air.", "box", mcCmds, ttsVoiceClips, contains)
  elif "barrel" in response:  # A storage container in Minecraft
    allocateToArrays("spawn shulker", "Spawning Shulkers to lift you up into the air.", "barrel", mcCmds, ttsVoiceClips, contains)

  # Warden
  if "dark" in response:  # Applies the "Darkness" effect on players
    allocateToArrays("spawn warden", "Spawning a Warden because you were too noisy.", "dark", mcCmds, ttsVoiceClips, contains)
  elif "warden" in response:
    allocateToArrays("spawn warden", "Spawning a Warden because you were too noisy.", "warden", mcCmds, ttsVoiceClips, contains)

  # Ender Dragon  
  if "dragon" in response:
    allocateToArrays("spawn dragon", "Spawning an Ender Dragon, good luck speedrunning that.", "dragon", mcCmds, ttsVoiceClips, contains)

  # Wither
  if "wither" in response:
    allocateToArrays("spawn wither", "Spawning a Wither to shoot skulls at you.", "wither", mcCmds, ttsVoiceClips, contains)

  # Just TNT.
  if "tnt" in response:
    allocateToArrays("spawn tnt", "Spawning TNT, kaboom.", "tnt", mcCmds, ttsVoiceClips, contains)

  print(res, end=" (Contains " if contains else "\n")
  for word in contains:
    if word == contains[-1]:
      print(word, end=")\n")
    else:
      print(word, end=", ")
  for cmd in ttsVoiceClips:
    playTTS(cmd)
  return mcCmds


while True:
  try:
    with mic as src:
      r.adjust_for_ambient_noise(src)
      audio = r.listen(src)
      resp = r.recognize_google(audio)
      cmd = getResponse(resp)

      mcInstance.stream(cmd)  # Send to Minecraft

  except sr.UnknownValueError:
    pass