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
		with open(scoreFile_name, "rb") as scoreFile:
			unpickled = pickle.Unpickler(scoreFile)
			scores = unpickled.load()
	else:
		scores = {}
	return scores

def save_scores(scores):
	"""this funstion saves scores in scoreFile_name, it gets scores as options"""

	with open(scoreFile_name, "wb") as scoreFile:
		unpickled = pickle.Pickler(scoreFile)
		unpickled.dump(scores)

# Word list management
def get_words():
	try:
		os.path.exists(wordList_name)
		with open(wordList_name, "r") as wordList:
			words = wordList.read()
			words = words.split('\n')
			#print("words")
	except:
		print("invalid word list")
		print("edit data.py with valid word list name")
		words = "invalid"
	return words


# input management

def get_userName():
	"""this function gets Username, the name should be at least 4 letters long, and only be composed of letters & numbers

if userName is invalid the fonction is called again until it is valid"""

	userName = input("Enter your name: ")
#(should be at least 4 letters long and and only be composed of letters & numbers)

	#1st letter in capital, others lowercase
	userName = userName.capitalize()
	if not userName.isalnum or len(userName)<4:
		print("Invalid user name")
		# function is called again
		return get_userName()
	else: 
		return userName

def get_letter():
	"""this function gets the letter given by user. if the string isn't a letter, then function is called again until a valid entry"""

	letter = input("Enter a letter: ")
	letter  =letter.upper()
	if len(letter)>1 or not letter.isalpha():
		print("Not a valid letter")
		return get_letter()
	else: 
		return letter

# Game functions

def choose_word():
	"""chooses a word in words"""
	words = get_words()
	return choice(words)

def get_hiddenWord(wholeWord, foundLetters):
	"""returns hidden word (whole or part), 
	- origin word (str)
	- already found letters (list)"""

	hiddenWord = ""
	for letter in wholeWord:
		if letter in foundLetters:
			hiddenWord += letter
		else :
			hiddenWord +="*"
	return hiddenWord




#help section
"""Displays help if asked"""
def help():
	print("Halp!")

