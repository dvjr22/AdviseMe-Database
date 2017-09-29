# Tables.py
# @author Diego Valdes
# Module to drop and add tables for AdviseMe db

# Just a few things I need to make this work
from mysql.connector import Error

""" ----------------------------------------------------------------------------------------------------------
Drops capstone db tables
"""
def dropTables(cursor):
	
	# Dictionary of drop statements
	drop = {}
	drop['curriculum'] = ("DROP TABLE curriculum;")
	drop['degree'] = ("DROP TABLE degree;")
	drop['enrolled'] = ("DROP TABLE enrolled;")
	drop['college'] = ("DROP TABLE college;")
	drop['classes'] = ("DROP TABLE classes;")
	drop['students'] = ("DROP TABLE students;")

	print ("Dropping AdviseMe Tables:")

	# Execute drop statements
	for index, query in drop.items():

		try:
			cursor.execute(query)

		except Error as e:
			print (e.msg)

		else:
			print ("Query: %s successful" %(query)) 


""" ----------------------------------------------------------------------------------------------------------
Create capstone tables for MySQL db
"""
def createTables(cursor):
	
	# Dictionary of create table statements
	tables = {}
	tables['students'] = (
		"CREATE TABLE `students` ("
		"  _id integer NOT NULL auto_increment,"
	    	"  sid varchar(9),"
		"  first varchar(30),"
		"  last varchar(30),"
		"  dob date,"
		"  status char(3),"
		"  hours smallint,"
		"  primary key (_id),"
		"  unique (sid)"
		");"
	)

	tables['classes'] = (
		"CREATE TABLE `classes` ("
		"  _id integer NOT NULL auto_increment,"
		"  prefix varchar(4),"
		"  co_num varchar(4),"
		"  title varchar(50),"
		"  hours tinyint,"
		"  primary key (_id),"
		"  unique (prefix, co_num)"
		");"
	)

	tables['college'] = (
		"CREATE TABLE `college` ("
		"  _id integer NOT NULL auto_increment,"
	    	"  college varchar(30),"
		"  major char(3),"
		"  primary key (_id),"
		"  unique (college, major)"
		");"
	)
	
	tables['enrolled'] = (
		"CREATE TABLE `enrolled` ("
		"  _id integer NOT NULL auto_increment,"
	    	"  sid varchar(9),"
		"  prefix varchar(4),"
		"  co_num varchar(4),"
		"  grade char(1),"
		"  primary key (_id),"
		"  unique (sid, prefix, co_num)"
		");"
	)
	
	tables['degree'] = (
		"CREATE TABLE `degree` ("
		"  _id integer NOT NULL auto_increment,"
	    	"  sid varchar(9),"
		"  major char(3),"
		"  primary key (_id),"
		"  unique (sid, major)"
		");"
	)

	tables['curriculum'] = (
		"CREATE TABLE `curriculum` ("
		"  _id integer NOT NULL auto_increment,"
		"  prefix varchar(4),"
		"  co_num varchar(4),"
	    	"  major char(3),"
		"  semester char(1),"
		"  min_grade char(1) default NULL,"
		"  primary key (_id),"
		"  unique (prefix, co_num, major)"
		");"
	)
	
	print ("Creating AdviseMe tables:")

	# Execute create statements
	for index, query in tables.items():

		try:
			cursor.execute(query)

		except Error as e:
			print (e.msg)

		else:
			print ("Query: %s \nsuccessful" %(query)) 



