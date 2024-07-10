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
    search = argv[4]
    query = """
        SELECT *
        FROM states
        WHERE states.name = %s
        ORDER BY states.id
        """
    cur.execute(query, (search,))

    """ Fetch all rows """
    rows = cur.fetchall()

    """ Printing each row """
    for row in rows:
        print("({}, '{}')".format(row[0], row[1]))

    """ Close the Cursor and the DB """
    cur.close()
    db.close()
