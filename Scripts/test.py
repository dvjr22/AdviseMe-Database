# test.py
# @author Diego Valdes
# Testing db modules

import sys
if '/home/valdeslab/SeniorYear/Capstone/Database/Scripts/Modules' not in sys.path:
	sys.path.append('/home/valdeslab/SeniorYear/Capstone/Database/Scripts/Modules')

from Connection import Connection
import Student

for i in range(0, 100):

	print(Student.firstName())
	print(Student.lastName())
	print(Student.sid())
	print(Student.birthday())
	print("--------------------------------------")


