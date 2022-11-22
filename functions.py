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
	argt = " ".join(args)
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