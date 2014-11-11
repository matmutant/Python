# -*-coding:Utf-8 -*
from data import *
from functions import *

# gettinf scores
scores = get_scores()
# getting words to be used
words = get_words()

# printing scores
print("scores: ", scores)
#print("list of words: ", words)

# getting userName :
user = get_userName()

#if user doesn't exist, then getting added
if user not in scores.keys():
	scores[user] = 0 #no points before the first game
continueGame = True

while continueGame :
	print("player {0}: {1} points".format(user, scores[user]))
	wordToFind = choose_word()
	print("word to find is", wordToFind)
	triedLetters = []
	foundLetters = []
	foundWord = get_hiddenWord(wordToFind, foundLetters)
	nbTries = nbRounds
	while wordToFind != foundWord and nbTries > 0:
		print("Word to Find {0} ({1} tries left)".format(foundWord, nbTries))
		print("already tried letters")
		print(triedLetters)
		letter = get_letter()
		if letter in foundLetters:
			print("already tried letter")
		elif letter in wordToFind:
			foundLetters.append(letter)
			print("well done!")
		else:
			nbTries -= 1
			print("No, that letter is no in that word")
			triedLetters.append(letter)
		foundWord = get_hiddenWord(wordToFind, foundLetters)
	if wordToFind == foundWord:
		print("congratulations! you found the word {0}.".format(wordToFind))
	else:
		print("Hanged!, you lose the game...")

	#updating user score
	scores[user] += nbTries

	#asking to re-play
	exit = str() #empty string created
	exit=input("do you wanna exit now? (y/n)")
	if exit.lower() == "y":
		continueGame=False

# Game ended, updating scores
save_scores(scores)

#displaying user scores : 
print("You end the game with {0} points.".format(scores[user]))








input("Press ENTER to exit...")
