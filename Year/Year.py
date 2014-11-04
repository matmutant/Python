# -*-coding:Utf-8 -*
year = input("type a year : ")

print(year)
try:
	year = int(year) #convert variable from string to integer
	assert year > 0
except ValueError:
	print("not a number")
except AssertionError:
	print("not a real year (<0)")
else:
	if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
		print("Leap Year")
	else:
		print("nope")
finally:
	input("Press ENTER to exit...")
