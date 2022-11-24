#!/usr/bin/env python3
"""
The inventory file for Tabloons creates and manages the inventory UI.
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
	print("A required internal module has failed to import.")
	exit() # Force quit normally, or error the code and quit via error if exit is not a function.

# Prevent running from main context
if __name__ == "__main__":
	errorExit(f"inventory.py must be ran from a non-main context, not a main context")

for module in modules:
	if not module == "functions.py":
		try:
			exec("import "+module)
			output(f"Imported {module}", context="import:invt")
		except Exception as e:
			errorExit(str(e))

# Window Creation
important = {}
objects = []
imagedump = []

def updateInventory(parent):
	from PIL import Image, ImageTk
	"""
	Create an updated inventory.
	"""
	clearInventoryUI()
	# Title Creation
	letterI = 0
	for letter in "inventory":
		letter0 = ImageTk.PhotoImage(eval(getFontChar(letter)))
		imagedump.append(letter0)
		letter1 = tkinter.Label(parent, image=letter0, bg="#4C2B0E")
		objects.append(letter1)
		letter1.place(x=4+(14*letterI), y=4, width=16, height=16)
		letterI += 1
	# Read Session File
	sessdata = {}
	with open(".session") as gip:
		for prl in gip:
			prl = prl.split("=")
			prl[1] = prl[1].replace("\n", "")
			sessdata[prl[0]] = prl[1]
	# Dabloon Count
	letterI = 0
	dbs = sessdata["dbs"]
	for letter in f"dabloons: ?{dbs}":
		if not letter in " ?":
			letter0 = ImageTk.PhotoImage(eval(getFontChar(letter)).resize((8, 8)))
			imagedump.append(letter0)
			letter1 = tkinter.Label(parent, image=letter0, bg="#4C2B0E")
		elif letter == "?":
			letter0 = ImageTk.PhotoImage(eval(getIcon('dabloon')).resize((8, 8), Image.ANTIALIAS))
			imagedump.append(letter0)
			letter1 = tkinter.Label(parent, image=letter0, bg="#4C2B0E")
		else:
			letter1 = tkinter.Label(parent, bg="#4C2B0E")
		objects.append(letter1)
		offset = 0
		if letter == "?": offset = 2
		letter1.place(x=4+((6*letterI)-offset), y=20, width=8, height=8)
		letterI += 1


def createWindow(parent):
	"""
	Create the game window.
	"""
	mainWindow = tkinter.Frame(parent, width=512, height=256, bg="#4C2B0E")
	important["window"] = mainWindow
	updateInventory(mainWindow)
	return mainWindow

def clearInventoryUI():
	global obj, imagedump
	"""
	Clear the current inventory UI.
	"""
	for obj in objects: obj.destroy()
	obj = []
	imagedump = []