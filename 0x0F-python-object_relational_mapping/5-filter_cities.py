#!/usr/bin/python3
"""
Write a script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()
    query = """SELECT cities.name
            FROM cities
            INNER JOIN states ON states.id = cities.state_id
            WHERE states.name = %s
            ORDER BY cities.id ASC"""
    state_name = sys.argv[4]
    cursor.execute(query, (state_name,))

    for row in cursor.fetchall():
        print(row[0])

    cursor.close()
    db.close()
