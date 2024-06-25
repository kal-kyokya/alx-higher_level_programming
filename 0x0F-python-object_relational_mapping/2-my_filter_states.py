#!/usr/bin/python3
"""
'2-my_filter_states' uses the module MySQLdb to
query the states table of our Database
for row of name matching an input string.

Usage:
./2-my_filter_states <mysql username> <mysql password>
		     <database name> <state name searched>
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cursor = db.cursor()

    query = f"SELECT * FROM states WHERE BINARY name LIKE '{sys.argv[4]}'"
    cursor.execute(query)

    for obj in cursor.fetchall():
        print(obj)
