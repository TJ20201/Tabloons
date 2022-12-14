#!/usr/bin/env python3
"""
The function file contains functions global across the entire Tabloons game.
This file is standalone and does not import any modules, except for the "sys" module.
"""
import sys

outputSeverity = {
	"MESSAGE": 0,
	"WARNING": 1,
	"ERROR": 2,
	"FATAL": 3
}
def output(*args, severity:int=outputSeverity["MESSAGE"], context:str="main"):
	"""
	Function for easy management of outputted messages (eg. error codes)
	Uses outputSeverity variable for severity of message and context for message origin context.
	"""
	svt = "MESSAGE"
	if severity == outputSeverity["WARNING"]: svt = "WARNING"
	if severity == outputSeverity["ERROR"]: svt = "ERROR"
	if severity == outputSeverity["FATAL"]: svt = "FATAL"
	argt = " ".join([str(arg) for arg in args])
	print(f"[{svt.upper()}][{context.upper()}] {argt}")

def errorExit(errorInfo: str = "Unexpected Error"):
	"""
	Function used for exiting the game due to an error within the code.
	Used only for when the error can not be resolved by the developer(s). (eg. uninstalled module)
	"""
	output("\n"*2)
	output("An error occured with the game and must exit. Information:", errorInfo)
	input("> Press Enter <")
	sys.exit(0)

def getFontChar(lett: str) -> str:
	"""
	Gets the PILLOW string for a character from the custom font.
	Returns: PILLOW string for eval()
	"""
	rows = {
		"1": "abcdefghijklmnop",
		"2": "qrstuvwxyz012345",
		"3": "6789$:"
	}
	left = upper = right = lower = 0
	if lett in rows["1"]: 
		upper = 0
		right = (rows["1"].rfind(lett)*8)+8
		left = right-8
		lower = upper+8
	if lett in rows["2"]: 
		upper = 8
		right = (rows["2"].rfind(lett)*8)+8
		left = right-8
		lower = upper+8
	if lett in rows["3"]: 
		upper = 16
		right = (rows["3"].rfind(lett)*8)+8
		left = right-8
		lower = upper+8
	ret = (left, upper, right, lower)
	#return ret
	return f"Image.open(f'./assets/font.png').crop({ret}).resize((16, 16), Image.ANTIALIAS)"

def getIcon(ico: str) -> str:
	"""
	Get a specific icon.
	Returns: STRING for eval()
	"""
	return f"Image.open(f'./assets/icon/{ico}.png')"