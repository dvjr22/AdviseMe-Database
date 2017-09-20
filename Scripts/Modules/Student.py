# Student.py
# @author Diego Valdes
# Module to create test student data for AdviseMe db

import random as r
import calendar as c


""" ----------------------------------------------------------------------------------------------------------
Generate a student id
"""
def sid():
	
	sid = r.choice('abcdefghijklmnopqrstuvwxyz')
	for i in range(0,8):
		sid += r.choice('1234567890')

	return sid
	

""" ----------------------------------------------------------------------------------------------------------
Generate a random first name
"""
def firstName():

	first = ["Bill", "Ted", "Peter", "Thomas", "Bruce", "Samuel", "Kevin", "Tyler", "Evan", "Ethan", 
		"Jean", "Cassandra", "Gwen", "Angelica", "Barbara", "Stacey", "Nikki", "August", "April", 
		"Ann", "Nick", "Patricia", "Mary Jane", "Kitty", "Casey", "Caleb", "Clark", "Bruce"]

	return first[r.randint(0, (len(first) - 1))]


""" ----------------------------------------------------------------------------------------------------------
Generate a random last name
"""
def lastName():

	last = ["Parker", "Wayne", "Stevens", "Cooper", "Thomas", "Smith", "Peterson", "Brady", "Rogers", 
		"Jordan", "Ewing", "Starks", "King", "Washington", "Cain", "Grayson", "Prince", "Gonzalez",
		"Gordon", "Jameson", "Holmes", "Cole", "Summers", "Connors", "Kent", "Morales"]

	return last[r.randint(0, (len(last) - 1))]


""" ----------------------------------------------------------------------------------------------------------
Generate a birthday
"""
def birthday():

	mon31 = [1, 3, 5, 7, 8, 10, 12]
	mon30 = [4, 6, 9, 11]
	
	month = r.randint(1, 12)
	year = r.randint(1980, 1998)
	
	if month in mon31:
		day = r.randint(1, 31)
	elif month in mon30:
		day = r.randint(1, 30)
	else:
		# if c.isleap(year):
		if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
			day = r.randint(1, 29)
		else:
			day = r.randint(1, 28)

	return str(year) +"-"+ str(month) + "-" + str(day)









