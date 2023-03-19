#!/usr/bin/python3
"""Script that takes in an argument and displays
    all values in the `states` table of `hbtn_0e_0_usa
    where name matches the argument.

    Script should be safe from MySQL injection.
"""
import sys
import MySQLdb


if __name__ == "__main__":
    # Store the argument values
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connecting to a MySQL database
    db = MySQLdb.connect(user=username, passwd=password, db=database)

    # Getting a Cursor
    cur = db.cursor()

    # Executing the MySQL Queries
    query_literal = "SELECT * FROM states WHERE name LIKE BINARY %s;"
    query = query_literal.format(state_name)
    cur.execute(query_literal, state_name)
    rows = cur.fetchall()
    for row in rows:
        print("{}".format(row))
    # Close all cursors
    cur.close()
    # Close all databases
    db.close()
