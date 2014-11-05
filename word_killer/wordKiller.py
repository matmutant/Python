# -*-coding:Utf-8 -*
wordToKill = input("enter word to kill: ")
Rampage = True
while Rampage:
	letterToKill = input("enter letter to remove: ")
	for i in wordToKill:
		if i == letterToKill:
			wordToKill = wordToKill.split(i)
			wordToKill = "".join(wordToKill)
	print(wordToKill)
	if wordToKill:
		print("letters left")
	else:
		print("Word nuked")
		Rampage = False
		continue
	continueGame = input("continue? (y/n)")
	if continueGame.lower() == "n":
		Rampage = False
input("Press ENTER to exit...")
