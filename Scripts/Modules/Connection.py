# Connection.py
# @author Diego Valdes
# Class to create a connection to MySQL db

# Stuff to borrow with full intention of returning
import mysql.connector as c
from mysql.connector import errorcode, Error

# Class to create MySQL connection objects
class Connection(object):

	""" --------------------------------------------------------------------------------------------------
	Class method
	Create and return a MySQL connection object
	** If you'd like to create the database from scratch, here is where you'd do that **
	"""
	def __new__(cls):

		# Open file with login information
		file = open('/home/valdeslab/SeniorYear/login', 'r')
		login = []

		# Add login info to array
		for line in file:
			login.append(line.strip())
	
		# Dictionary of connection args
		config = {
			'user'		:	login[0],
			'password'	:	login[1],
			'database'	:	login[2]
		}

		try:
			# Create connection with args
			conn = c.connect(**config)
			return conn

		except Error as e:

			if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
				print("Login credentials are bad")
			elif e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
				print("Database does not exist")
			else:
				print(e)

		



