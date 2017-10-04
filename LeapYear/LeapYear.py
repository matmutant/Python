#!/usr/bin/python3
import calendar


YearStart = 1992
YearEnd = 2017

def isLeap(YearStart,YearEnd):
	for year in range(YearStart,YearEnd+1, 1):
		four = (year%4==0)
		hundred = (year%100==0)
		fourHundred = (year%400==0)
		#print(year)
		#print(four, hundred, fourHundred)
		Leaping = (four and not hundred or fourHundred)
		print ("the year {} is {} (verif:{})".format(year,Leaping,calendar.isleap(year)))

isLeap(YearStart,YearEnd)
