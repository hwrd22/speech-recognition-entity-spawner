# Minecraft Speech Recognition Entity Spawner (Fabric)
A Minecraft: Java Edition mod that has two components: A voice recognition program, and a Minecraft: Java Edition mod.<br><br>
The Voice Recognition program will take microphone input from the user and use Google's Speech-To-Text technology to convert audio to text, and then will check for key words to send commands to Minecraft.<br><br>
The Fabric mod will take commands from the Voice Recognition program and will cause events to occur ingame. In this mod's case, will spawn the relevant entity.

## Requirements:
- Minecraft: Java Edition 1.21.5
  - Fabric Modloader for Minecraft 1.21.5, as well as the Fabric API mod
### If using the `.py` Files
- Python 3.12
- pip
- The following Python libraries (If not already installed):
  - speech_recognition
  - gtts
  - playsound
### If using the `.exe` File:
- Nothing more. However, `.exe` will only work on Windows.

## Usage
- Take the `.jar` file in Releases and place it into your mods directory (`C:/%appdata%/.minecraft/mods` by default on Windows)
- Take the `data` directory and both `.py` files (or the `.exe` file) and place them into their own directory, preferably where it is easy to access.
- Launch Minecraft: Java Edition 1.21.5 with the Fabric modloader and the mod installed first. The Voice Recognition program requires that Minecraft is running with the mod.
  - If you are unaware of how to mod Minecraft, refer to YouTube guides.
- Once Minecraft is finished launching, run `speech-recog.py` using Python (or `speech-recog.exe` if you downloaded the `.exe`. Python is not needed for this method), preferably with a microphone plugged in.

## List of Mobs and Their Default Keywords
<table>
  <tr>
    <th>Mob/Entity</th>
    <th>Key words</th>
  </tr>
  <tr><td>Bee</td><td><code>'bee'</code>, <code>'honey'</code></td></tr>
  <tr><td>Iron Golem</td><td><code>'iron'</code>, <code>'town'</code>, <code>'village'</code></td></tr>
  <tr><td>Polar Bear</td><td><code>'bear'</code>, <code>'ice'</code></td></tr>
  <tr><td>Wolf</td><td><code>'dog'</code>, <code>'wolf'</code></td></tr>
  <tr><td>Blaze</td><td><code>'blaze'</code>, <code>'fire'</code></td></tr>
  <tr><td>Breeze</td><td><code>'breeze'</code>, <code>'wind'</code></td></tr>
  <tr><td>Creeper</td><td><code>'cat'</code>, <code>'creeper'</code>, <code>'hiss'</code></td></tr>
  <tr><td>Enderman</td><td><code>'carry'</code>, <code>'end'</code></td></tr>
  <tr><td>Endermite</td><td><code>'mite'</code>, <code>'pearl'</code></td></tr>
  <tr><td>Ghast</td><td><code>'ghast'</code>, <code>'ghost'</code>, <code>'soul'</code></td></tr>
  <tr><td>Guardian</td><td><code>'guard'</code>, <code>'ocean'</code>, <code>'sea'</code></td></tr>
  <tr><td>Hoglin</td><td><code>'hog'</code>, <code>'warp'</code></td></tr>
  <tr><td>Magma Cube</td><td><code>'magma'</code>, <code>'lava'</code></td></tr>
  <tr><td>Phantom</td><td><code>'bed'</code>, <code>'phantom'</code>, <code>'sleep'</code></td></tr>
  <tr><td>Piglin</td><td><code>'gold'</code>, <code>'pig'</code></td></tr>
  <tr><td>Piglin Brute</td><td><code>'axe'</code>, <code>'brute'</code>, <code>'treasure'</code></td></tr>
  <tr><td>Pillager</td><td><code>'illager'</code>, <code>'totem'</code></td></tr>
  <tr><td>Ravager</td><td><code>'raid'</code>, <code>'ravager'</code></td></tr>
  <tr><td>Shulker</td><td><code>'barrel'</code>, <code>'box'</code>, <code>'chest'</code>, <code>'shulker'</code></td></tr>
  <tr><td>Silverfish</td><td><code>'fish'</code>, <code>'hold'</code>, <code>'silver'</code>, <code>'stone'</code>, <code>'strong'</code></td></tr>
  <tr><td>Skeleton</td><td><code>'bone'</code>, <code>'bow'</code>, <code>'skeleton'</code></td></tr>
  <tr><td>Slime</td><td><code>'block'</code>, <code>'cube'</code>, <code>'slime'</code></td></tr>
  <tr><td>Spider</td><td><code>'bug'</code>, <code>'spider'</code></td></tr>
  <tr><td>Witch</td><td><code>'brew'</code>, <code>'hut'</code>, <code>'pot'</code>, <code>'witch'</code></td></tr>
  <tr><td>Wither Skeleton</td><td><code>'coal'</code>, <code>'skull'</code></td></tr>
  <tr><td>Zombie</td><td><code>'brain'</code>, <code>'dead'</code>, <code>'die'</code>, <code>'rot'</code>, <code>'zombie'</code></td></tr>
  <tr><td>Ender Dragon</td><td><code>'dragon'</code>, <code>'egg'</code></td></tr>
  <tr><td>Warden</td><td><code>'ancient'</code>, <code>'city'</code> <code>'dark'</code>, <code>'deep'</code> <code>'warden'</code></td></tr>
  <tr><td>Wither</td><td><code>'nether'</code>, <code>'star'</code>, <code>'three'</code>, <code>'wither'</code></td></tr>
  <tr><td>TNT</td><td><code>'boom'</code>, <code>'tnt'</code></td></tr>
</table>
