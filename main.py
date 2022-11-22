#!/usr/bin/env python3
"""
The main file for Tabloons loads up the window and initial game settings. Subwindows such as the game which get displayed
in a section of the window (eg. top left) will be inside of an external file with the same import method to the main file.
"""

# Prevent running from non-main context
if __name__ != "__main__":
	errorExit(f"main.py must be ran from a main context, not another process under main context")

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

for module in modules:
	if not module == "functions.py":
		try:
			exec("import "+module)
			output(f"Imported {module}", context="import")
		except Exception as e:
			errorExit(str(e))

# Window Creation
clearableElements = {
	"game": [],
	"inventory": []
}
importantElements = clearableElements
mainWindow = tkinter.Tk()
mainWindow.geometry("512x512")
mainWindow.title(properties["gameName"]+" v"+properties["versionString"])
mainWindow.configure(bg='#000000')

# Window Management
def clearElements(subject: str):
	"""
	Function to clear all clearable elements within a specific part of the window (such as the game window)
	"""
	amt = 0
	for ce in clearableElements[subject]:
		amt = amt + 1
		ce.destroy()
	output(f"Cleared {amt} clearable elements from {subject} class", context="game")

# Begin Game
mainWindow.mainloop()
