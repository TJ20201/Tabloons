#!/usr/bin/env python3
"""
The main file for Tabloons loads up the window and initial game settings. Subwindows such as the game which get displayed
in a section of the window (eg. top left) will be inside of an external file with the same import method to the main file.
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
	import game
	import inventory
except Exception as e:
	print("A required internal module has failed to import.")
	exit() # Force quit normally, or error the code and quit via error if exit is not a function.

# Prevent running from non-main context
if __name__ != "__main__":
	errorExit(f"main.py must be ran from a main context, not another process under main context")

for module in modules:
	if not module == "functions.py":
		try:
			exec("import "+module)
			output(f"Imported {module}", context="import:main")
		except Exception as e:
			errorExit(str(e))

from PIL import Image, ImageTk

# Create Session File
if (os.path.exists(".session")):
	os.remove(".session")
with open(".session", "a") as sessfile:
	sessfile.write("dbs=0\ninv=[]")

# Create save folder if non-existant
if not os.path.exists("./saves"):
	output("Creating new saves folder...")
	os.mkdir("saves")
else:
	output("Save folder already exists, skipping creation")

# Window Creation
mainWindow = tkinter.Tk()
mainWindow.geometry("512x512")
mainWindow.title(properties["gameName"]+" v"+properties["versionString"])
mainWindow.configure(bg='#000000')
mainWindow.bind("<KeyPress>", game.keybinds)

imagedump = []

gameFrame = game.createWindow(mainWindow)
gameFrame.place(x=0,y=0,width=256,height=256)

inventoryFrame = inventory.createWindow(mainWindow)
inventoryFrame.place(x=0,y=256,width=512,height=256)

# Create Ingame Menu
menuFrame = tkinter.Frame(mainWindow, width=256, height=256, bg="#000000")
menuFrame.place(x=256,y=0,width=256,height=256)
# Pause Button
pauseButton = []
def pause(event):
	output("Pause button test.")
letterI = 0
for letter in "pause":
	letter0 = ImageTk.PhotoImage(eval(getFontChar(letter)))
	imagedump.append(letter0)
	letter1 = tkinter.Label(menuFrame, image=letter0, bg="#111111")
	pauseButton.append(letter1)
	letter1.place(x=(4+(28*letterI))+(128-(5*16)), y=40, width=36, height=36)
	letter1.bind("<Button-1>", pause)
	letterI += 1
# Save Button
saveButton = []
def saveGame(event):
	output("Save button test.")
letterI = 0
for letter in "save":
	letter0 = ImageTk.PhotoImage(eval(getFontChar(letter)))
	imagedump.append(letter0)
	letter1 = tkinter.Label(menuFrame, image=letter0, bg="#111111")
	saveButton.append(letter1)
	letter1.place(x=(4+(28*letterI))+(128-(4*16)), y=80, width=36, height=36)
	letter1.bind("<Button-1>", saveGame)
	letterI += 1
# Load Button
loadButton = []
def loadSave(event):
	output("Load button test.")
letterI = 0
for letter in "load":
	letter0 = ImageTk.PhotoImage(eval(getFontChar(letter)))
	imagedump.append(letter0)
	letter1 = tkinter.Label(menuFrame, image=letter0, bg="#111111")
	saveButton.append(letter1)
	letter1.place(x=(4+(28*letterI))+(128-(4*16)), y=120, width=36, height=36)
	letter1.bind("<Button-1>", loadSave)
	letterI += 1
# Quit Button
quitButton = []
def windowExitMethod(*args):
	if (os.path.exists(".session")):
		os.remove(".session")
	mainWindow.destroy()
letterI = 0
for letter in "quit":
	letter0 = ImageTk.PhotoImage(eval(getFontChar(letter)))
	imagedump.append(letter0)
	letter1 = tkinter.Label(menuFrame, image=letter0, bg="#111111")
	saveButton.append(letter1)
	letter1.place(x=(4+(28*letterI))+(128-(4*16)), y=160, width=36, height=36)
	letter1.bind("<Button-1>", windowExitMethod)
	letterI += 1

# Begin Game
mainWindow.protocol("WM_DELETE_WINDOW", windowExitMethod)
mainWindow.mainloop()