# -*-coding:Utf-8 -*
from math import ceil
from random import randrange
"""this program ask for initial $ amount, number choosen and then plays with random numbers"""

amount=1000 #initial amount of money
continueGame=True #boolean that stay true as long as player wanna play
print("take a seat and play, amount of money:", amount,"$")

while continueGame:
	#set up the number choosen by player
	choosenNumber=-1
	while choosenNumber < 0 or choosenNumber > 49:	
		choosenNumber=input("type a number between 0 and 49: ")
		try:
			choosenNumber=int(choosenNumber)
		except ValueError:
			print("not a number")
			continue
		if choosenNumber <0:
			print("<0")
		if choosenNumber > 49:
			print(">49")

	#set up amount of money choosen by player
	choosenAmount=0
	while choosenAmount <= 0 or choosenAmount > amount:
		choosenAmount = input("choose amount:")	
		try:
			choosenAmount=int(choosenAmount)
		except ValueError:
			print("not a number")
			choosenAmount = -1
		if choosenAmount <= 0:
			print("<=0")
		if choosenAmount > amount:
			print("You don't have that much money! only", amount,"$ left")
	
	#randomising...
	roulette=randrange(50)
	print("letting things go ... done: ", roulette)
	
	#loose/win
	if roulette == choosenNumber:
		print("congratulation, you won", choosenAmount*3, "$!")
		amount += choosenAmount*3
	elif roulette % 2 == choosenNumber % 2:
		choosenAmount = ceil(choosenAmount * 0.5)
		print("congratulation, you get the same color, you won", choosenAmount, "$!")
		amount += choosenAmount
	else:
		print("sorry, not this time")
		amount -= choosenAmount
	#game ends if player is ruined
	if amount <= 0:
		print("no more money, get out of here!")
		continueGame = False
	else:
		print(amount,"$ left")
		exit=input("do you wanna exit now? (y/n)")
		if exit == "y" or exit == "Y":
			print("you are leaving the game with", amount,"$")
			continueGame=False

input("Press ENTER to exit...")
