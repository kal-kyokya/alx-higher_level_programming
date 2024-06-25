#!/usr/bin/python3
"""
'1-filter_states' uses the module MySQLdb to
query the states table of our Database using 'BINARY'
to enforce Case-sensitivity.

Usage:
./1-filter_states <mysql username> <mysql password> <database name>
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE BINARY name LIKE 'N%'"
    cursor.execute(query)

    for obj in cursor.fetchall():
        print(obj)
