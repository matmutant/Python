# -*-coding:Utf-8 -*
year = input("type a year : ")
year = int(year) #convert variable from string to integer
print(year)
leap = False
if year % 4 == 0:
	if year % 100 == 0:
		if year % 400 == 0:
			leap=True
		else:
			leap = False
	else:
		leap = True
else:
	leap = False

if leap:
	print("Leap Year")
else:
	print("nope")

input("Press ENTER to exit...")
