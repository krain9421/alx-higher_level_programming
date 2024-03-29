#!/usr/bin/python3
"""Script that lists all states with a name
    starting with `N` from database hbtn_0e_0_usa.
"""
import sys
import MySQLdb


if __name__ == "__main__":
    # Store the argument values
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connecting to a MySQL database
    db = MySQLdb.connect(user=username, passwd=password, db=database)

    # Getting a Cursor
    cur = db.cursor()

    # Executing the MySQL Queries
    # cur.execute("SELECT * FROM `states` WHERE name LIKE 'N%';")
    cur.execute("SELECT * FROM `states` ORDER BY `id`;")
    rows = cur.fetchall()
    for row in rows:
        if row[1][0] == 'N':
            print("{}".format(row))
    # Close all cursors
    cur.close()
    # Close all databases
    db.close()
