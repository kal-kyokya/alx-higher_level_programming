#!/usr/bin/python3
"""
'3-my_safe_filter_states' uses the module MySQLdb to
safely query the states table of our Database
for row of name matching an injection averse input string.

Usage:
./3-my_safe_filter_states <mysql username> <mysql password>
                <database name> <state name searched>
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cursor = db.cursor()

    query = """SELECT *
               FROM states
               WHERE name LIKE BINARY %s
               ORDER BY states.id ASC"""
    input_value = sys.argv[4]
    cursor.execute(query, (input_value,))

    for obj in cursor.fetchall():
        print(obj)
