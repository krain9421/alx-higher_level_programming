#!/usr/bin/python3
# Script that lists all states from database hbtn_0e_0_usa
import sys
import MySQLdb as sql

# Store the argument values
username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

# Connecting to a MySQL database
db = sql.connect(host="3306", user=username, passwd=password, db=database)

# Getting a Cursor
cur = db.cursor()

# Executing the MySQL Queries
curr.execute("SELECT `name` FROM states ORDER BY `id` DESC;")
rows = c.fetchall()
print(state) for state in rows
