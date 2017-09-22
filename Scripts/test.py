# test.py
# @author Diego Valdes
# Testing db modules

import sys
if '/home/valdeslab/SeniorYear/Capstone/Database/Scripts/Modules' not in sys.path:
	sys.path.append('/home/valdeslab/SeniorYear/Capstone/Database/Scripts/Modules')

from Connection import Connection
import Student
import csv

'''
for i in range(0, 100):

	print(Student.firstName())
	print(Student.lastName())
	print(Student.sid())
	print(Student.birthday())
	print("--------------------------------------")

'''
# Field names: prefix, co_num, title, hours
with open('/home/valdeslab/SeniorYear/Capstone/Database/Data/classes.csv') as file:

	read = csv.DictReader(file)
	for row in read:
		print(row['prefix'], row['title'])

# Field names: prefix, co_num, major, semester
with open('/home/valdeslab/SeniorYear/Capstone/Database/Data/curriculum.csv') as file:

	read = csv.DictReader(file)
	for row in read:


#Field names: college, major
with open('/home/valdeslab/SeniorYear/Capstone/Database/Data/college.csv') as file:

	read = csv.DictReader(file)
	for row in read:
		


