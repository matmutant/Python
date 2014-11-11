# -*-coding:Utf-8 -*
from data import *
from functions import *

# gettinf scores
scores = get_scores()
# getting words to be used
words = get_words()

# printing scores
print("Scores: ", scores)
#print("list of words: ", words)

# getting userName :
user = get_userName()

#if user doesn't exist, then getting added
if user not in scores.keys():
	scores[user] = 0 #no points before the first game
continueGame = True

while continueGame :
	print("Player {0}: {1} points".format(user, scores[user]))
	wordToFind = choose_word()
	#uncomment the following ligne for testing purpose
	#print("word to find is", wordToFind)
	triedLetters = []
	foundLetters = []
	foundWord = get_hiddenWord(wordToFind, foundLetters)
	nbTries = nbRounds
	while wordToFind != foundWord and nbTries > 0:
		print("Word to Find {0} ({1} tries left)".format(foundWord, nbTries))
		print("Already tried letters: ", triedLetters)
		print("")
		letter = get_letter()
		if letter in foundLetters or letter in triedLetters:
			print("You already tried this letter")
		elif letter in wordToFind:
			foundLetters.append(letter)
			print("well done!")
		else:
			nbTries -= 1
			print("No, that letter is not in that word")
			triedLetters.append(letter)
		foundWord = get_hiddenWord(wordToFind, foundLetters)
	if wordToFind == foundWord:
		print("Congratulations! you found the word {0}.".format(wordToFind))
	else:
		print("Hanged!, you lose the game...")
		print("The word was {0}.".format(wordToFind))
	
	#updating user score
	scores[user] += nbTries

	#asking to re-play
	exit = str() #empty string created
	exit=input("Do you wanna exit now? (y/n)")
	if exit.lower() == "y":
		continueGame=False

# Game ended, updating scores
save_scores(scores)

# Displaying user scores : 
print("You end the game with {0} points.".format(scores[user]))

# Prompt exit
input("Press ENTER to exit...")
