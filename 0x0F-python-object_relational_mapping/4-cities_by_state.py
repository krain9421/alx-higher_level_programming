#!/usr/bin/python3
"""Script that lists all cities from the database
    hbtn_0e_4_usa
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
    query_literal = "SELECT city.id, city.name, state.name \
            FROM cities as city \
            INNER JOIN states as state \
            ON city.state_id = state.id \
            ORDER BY city.id;"
    cur.execute(query_literal)
    rows = cur.fetchall()
    for row in rows:
        print("{}".format(row))
    # Close all cursors
    cur.close()
    # Close all databases
    db.close()
