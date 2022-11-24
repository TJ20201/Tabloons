#!/usr/bin/env python3
"""
The game file for Tabloons creates and manages the actual game.
"""

# Read Properties File
properties = {}
with open("gameInfo.properties") as gip:
	for prl in gip:
		prl = prl.split("=")
		prl[1] = prl[1].replace("\n", "")
		properties[prl[0]] = prl[1]

# Module Imports
modules = [module for module in properties["requirements"].split(",")]
try:
	from functions import *
except Exception as e:
	print("A required module has failed to import.")
	exit() # Force quit normally, or error the code and quit via error if exit is not a function.

# Prevent running from main context
if __name__ == "__main__":
	errorExit(f"game.py must be ran from a non-main context, not a main context")

for module in modules:
	if not module == "functions.py":
		try:
			exec("import "+module)
			output(f"Imported {module}", context="import")
		except Exception as e:
			errorExit(str(e))

# Window Creation
important = {}
objects = []
imagedump = []

impcache = {
	"player": {
		"loc": (128, 128),
		"dir": "up"
	}
}

def updateScene(parent):
	"""
	Create an updated scene.
	"""
	createPlayer(parent, impcache["player"]["dir"])

def createWindow(parent):
	"""
	Create the game window.
	"""
	mainWindow = tkinter.Frame(parent, width=256, height=256, bg="#FFFFFF")
	important["window"] = mainWindow
	updateScene(mainWindow)
	return mainWindow

def clearScene():
	global obj, imagedump
	"""
	Clear the current game scene.
	"""
	for obj in objects: obj.destroy()
	imagedump = []

def cropArgsFromDirection(direction:str):
	"""
	Get the crop arguments from direction.
	"""
	if direction == "up": return (0, 0, 16, 16)
	if direction == "down": return (16, 0, 32, 16)
	if direction == "left": return (32, 0, 48, 16)
	if direction == "right": return (48, 0, 64, 16)
	return (0, 0, 16, 16) # If nothing found, return first 16x16 pixels.

def createPlayer(parent, direction:str, skin:str="template"):
	from PIL import Image, ImageTk
	"""
	Create the player object.
	"""
	# Prevent out of bounds
	if impcache["player"]["loc"][0] <= 0: impcache["player"]["loc"] = (216, impcache["player"]["loc"][1])
	if impcache["player"]["loc"][0] >= 224: impcache["player"]["loc"] = (8, impcache["player"]["loc"][1])
	if impcache["player"]["loc"][1] <= 0: impcache["player"]["loc"] = (impcache["player"]["loc"][0], 216)
	if impcache["player"]["loc"][1] >= 224: impcache["player"]["loc"] = (impcache["player"]["loc"][0], 8)

	tkimage = ImageTk.PhotoImage(Image.open(f'./assets/character/{skin}.png').crop(cropArgsFromDirection(direction)))
	imagedump.append(tkimage)
	player = tkinter.Label(parent, image=tkimage)
	objects.append(player)
	player.place(x=impcache["player"]["loc"][0]+8, y=impcache["player"]["loc"][1]+8, width=16, height=16)

# Keybinds
def keybinds(inp):
	cr = inp.char
	if cr in "wsad":
		clearScene()
		canpress = 0
	if cr == "w":
		impcache["player"]["loc"] = (impcache["player"]["loc"][0], impcache["player"]["loc"][1]-8)
		impcache["player"]["dir"] = "up"
		updateScene(important["window"])
	if cr == "s":
		impcache["player"]["loc"] = (impcache["player"]["loc"][0], impcache["player"]["loc"][1]+8)
		impcache["player"]["dir"] = "down"
		updateScene(important["window"])
	if cr == "a":
		impcache["player"]["loc"] = (impcache["player"]["loc"][0]-8, impcache["player"]["loc"][1])
		impcache["player"]["dir"] = "left"
		updateScene(important["window"])
	if cr == "d":
		impcache["player"]["loc"] = (impcache["player"]["loc"][0]+8, impcache["player"]["loc"][1])
		impcache["player"]["dir"] = "right"
		updateScene(important["window"])

