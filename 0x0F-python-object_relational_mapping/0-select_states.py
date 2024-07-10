#!/usr/bin/python3

from sys import argv
import MySQLdb

"""
This module demonstrates using Python with MySQL
"""


""" Establishing connection to the database """
db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                     db=argv[3], port=3306)
cur = db.cursor()

""" Executing the Query """
cur.execute("SELECT * FROM states ORDER BY states.id")

""" Fetch all rows """
rows = cur.fetchall()

""" Printing each row """
for row in rows:
    print("({}, '{}')".format(row[0], row[1]))

""" Close the Cursor and the DB """
cur.close()
db.close()

if __name__ == "__main__":
    pass
