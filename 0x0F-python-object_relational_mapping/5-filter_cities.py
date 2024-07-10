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
query = """
    SELECT cities.name AS city_name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id
    """
state_name = argv[4]
cur.execute(query, (state_name,))

""" Fetch all rows """
rows = cur.fetchall()

""" Printing each row """
city_names = [row[0] for row in rows]
print(", ".join(city_names))

""" Close the Cursor and the DB """
cur.close()
db.close()

if __name__ == "__main__":
    pass
