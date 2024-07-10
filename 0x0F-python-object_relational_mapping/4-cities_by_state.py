#!/usr/bin/python3

"""
This module demonstrates using Python with MySQL
"""


from sys import argv
import MySQLdb

if __name__ == "__main__":
    """ Establishing connection to the database """

    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306)
    cur = db.cursor()

    """ Executing the Query """
    query = """
        SELECT cities.id AS city_id, cities.name AS city_name,
        states.name AS state_name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id
        """
    cur.execute(query)

    """ Fetch all rows """
    rows = cur.fetchall()

    """ Printing each row """
    for row in rows:
        print("({}, '{}', '{}')".format(row[0], row[1], row[2]))

    """ Close the Cursor and the DB """
    cur.close()
    db.close()
