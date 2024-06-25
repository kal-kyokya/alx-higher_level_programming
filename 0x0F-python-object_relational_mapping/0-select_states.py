#!/usr/bin/python3
"""
'0-select_states' the module MySQLdb to query all states found in our Database

Usage:
./0-select_states <mysql username> <mysql password> <database name>
"""
import MySQLdb
import sys


if "__name__" == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cursor = db.cursor()

    query = "SELECT * FROM states"
    cursor.execute(query)

    for obj in cursor.fetchall():
        print(obj)
