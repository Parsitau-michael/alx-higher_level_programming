#!/usr/bin/python3

"""This module demonstrates using Python with MySQL
"""


from sys import argv
import MySQLdb


if __name__ == "__main__":
    username, password, dbase = argv[1], argv[2], argv[3]

    """ Establishing connection to the database """
    db = MySQLdb.connect(
                         host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=dbase)
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
