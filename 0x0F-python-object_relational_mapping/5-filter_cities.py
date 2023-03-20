#!/usr/bin/python3
"""Script that prints all cities of a database.
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
    query_literal = "SELECT cities.name FROM cities \
            INNER JOIN states \
            ON cities.state_id = states.id \
            WHERE CAST(states.name AS BINARY) = %s \
            ORDER BY cities.id ASC;"
    cur.execute(query_literal, state_name)
    rows = cur.fetchall()
    for row in rows:
        print("{}".format(row))
    # Close all cursors
    cur.close()
    # Close all databases
    db.close()
