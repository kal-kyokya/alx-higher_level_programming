#!/usr/bin/python3
"""
'1-filter_states' uses the module MySQLdb to query all states of our Database starting with 'N' (Capital N).

Usage:
./1-filter_states <mysql username> <mysql password> <database name>
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name LIKE 'N%'"
    cursor.execute(query)

    for obj in cursor.fetchall():
        print(obj)
