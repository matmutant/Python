# -*-coding:Utf-8 -*
year = input("type a year : ")
year = int(year) #convert variable from string to integer
print(year)
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
	print("Leap Year")
else:
	print("nope")

input("Press ENTER to exit...")
