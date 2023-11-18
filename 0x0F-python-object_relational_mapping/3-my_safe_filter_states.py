#!/usr/bin/python3
"""
return matching states with avoiding the sql injection
parameters given to script: username, password, database, state to match
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cursor = db.cursor()
    query = """SELECT *
                 FROM states
                 WHERE name LIKE %s ORDER BY id ASC"""
    state_name = argv[4]
    cursor.execute(query, (state_name,))
    for row in cursor.fetchall():
        print(row)
