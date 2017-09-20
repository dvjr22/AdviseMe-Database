# create_db.py
# @author Diego Valdes
# Creates the tables for the AdviseMe db

import sys
if '/home/valdeslab/SeniorYear/Capstone/Database/Scripts/Modules' not in sys.path:
	sys.path.append('/home/valdeslab/SeniorYear/Capstone/Database/Scripts/Modules')

from Connection import Connection
import Tables


# Create db connection
conn = Connection()
# Create cursor
cursor = conn.cursor()

# Drop old tables
Tables.dropTables(cursor)

# Create new tables
Tables.createTables(cursor)

# Close cursor
cursor.close()
# Close db connection
conn.close()
