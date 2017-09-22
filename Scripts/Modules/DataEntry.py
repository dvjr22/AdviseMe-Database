# DataEntry.py
# Handles data entry into AdviseMe db

from mysql.connector import Error

""" ----------------------------------------------------------------------------------------------------------

""" 
def insert(conn, query, data):

	# Create cursor
	cursor = conn.cursor()

	# Try block to catch insert errors
	try:
		# Insert data and commit
		cursor.execute(query, data)
		conn.commit()
		print(query + "successful")
			
	except Error as e:
		print(e)

	# Close cursor
	cursor.close()


