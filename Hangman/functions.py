"""this file defines functions used in Hangman game
it uses data stored in data.py"""

import os
import pickle
from random import choice
from data import *

# Score management
def get_scores():
	"""this function gets scores if file exits
	by the way it will return an associative array
	either the depickled object
	or an empty array."""
	
	if os.path.exists(scoreFile_name):
		with open(scoreFile_Name, "rb") as scoreFile:
			unpickled = pickle.Unpickler(scoreFile)
			scores = unpickled.load()
	else:
		scores = {}
	return scores

# Word list management
def get_words():
	try:
		os.path.exists(wordList_name)
		with open(wordList_name, "r") as wordList:
			words = wordList.read()
			words = words.split('\n')
			print("words")
	except:
		print("invalid word list")
		print("edit data.py with valid word list name")
		words = "invalid"
	return words
		


#help section
"""Displays help if asked"""
def help():
	print("Halp!")

