# test.py
# @author Diego Valdes
# Testing db modules

import sys
if '/home/valdeslab/SeniorYear/Capstone/Database/Scripts/Modules' not in sys.path:
	sys.path.append('/home/valdeslab/SeniorYear/Capstone/Database/Scripts/Modules')

from Connection import Connection
import Student, DataEntry
import csv

# Initialize db connection
conn = Connection()

# File locations and respective insert statements
classFile = '/home/valdeslab/SeniorYear/Capstone/Database/Data/classes.csv'
classesQ = ("INSERT INTO classes"
	"(prefix, co_num, title, hours)"
	"VALUES (%s, %s, %s, %s);")

curriculumFile = '/home/valdeslab/SeniorYear/Capstone/Database/Data/curriculum.csv'
curriculumQ = ("INSERT INTO curriculum"
	"(prefix, co_num, major, semester, min_grade)"
	"VALUES (%s, %s, %s, %s, %s);")

collegeFile = '/home/valdeslab/SeniorYear/Capstone/Database/Data/college.csv'
collegeQ = ("INSERT INTO college"
	"(college, major)"
	"VALUES (%s, %s);")

numStudents = 100

# Insert statement for students
studentsQ = ("INSERT INTO students"
	"(sid, first, last, dob, status)"
	"VALUES (%s, %s, %s, %s, %s)")


addMajor = ("INSERT INTO degree"
	"(sid, major)"
	"VALUES (%s, %s)")

# Field names: prefix, co_num, title, hours
with open(classFile) as file:

	read = csv.DictReader(file)
	for row in read:
		data = (row['prefix'], row['co_num'], row['title'], row['hours'])
		DataEntry.insert(conn, classesQ, data)


# Field names: prefix, co_num, major, semester
with open(curriculumFile) as file:

	read = csv.DictReader(file)
	for row in read:
		data = (row['prefix'], row['co_num'], row['major'], row['semester'], row['mingrade'])
		DataEntry.insert(conn, curriculumQ, data)



# Field names: college, major
with open(collegeFile) as file:

	read = csv.DictReader(file)
	for row in read:
		data = (row['college'], row['major'])
		DataEntry.insert(conn, collegeQ, data)


# Add 
for i in range(0, numStudents):
	
	sid = Student.sid()

	data = (sid, Student.firstName(), Student.lastName(), Student.birthday(), 'UND')
	DataEntry.insert(conn, studentsQ, data)

	data = (sid, Student.major())
	DataEntry.insert(conn, addMajor, data)


# get the list of sid - something seems to be broken about this
# getSid = ("SELECT sid from students;")
# sid = DataEntry.querySid(conn, getSid)


	









