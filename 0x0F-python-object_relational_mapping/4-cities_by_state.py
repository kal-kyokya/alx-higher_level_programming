#!/usr/bin/python3
"""
'4-cities_by_states' uses the module MySQLdb to query all cities of Database

Usage:
./4-cities_by_states <mysql username> <mysql password> <database name>
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cursor = db.cursor()

    query = """SELECT cities.id, cities.name, states.name
               FROM cities
               JOIN states
               ON cities.state_id = states.id
               ORDER BY cities.id ASC"""
    cursor.execute(query)

    for obj in cursor.fetchall():
        print(obj)
