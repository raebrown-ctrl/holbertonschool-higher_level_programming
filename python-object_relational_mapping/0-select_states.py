#!/usr/bin/python3
"""
lists all states from the database
"""
import MySQLdb
from sys import argv


def main(username, passwd, db):
    """
    list  must be sorted in ascending order by states.id
    """
    conn = MySQLdb.connect(
        host='localhost',
        user=username,
        password=passwd,
        database=db,
        port=3306
    )
    """
    CREATE A CURSOR OBJECT FOR EXECUTE ALL THE QUERIES WE NEED IT
    """
    c = conn.cursor()

    """ TO USE SQL COMMANDE AND EXECUTE IT  """
    c.execute("SELECT id, name FROM states ORDER BY id ASC")

    """
    fetchall is a method that fetches all the remaining tuples
    from the last executed statemebts from a table
    This method only returns the first row from the defined table
    and If there are no tuples then it returns an empty list in the output
    """
    rows = c.fetchall()

    for eachRow in rows:
        print(eachRow)


if __name__ == '__main__':
    main(argv[1], argv[2], argv[3])
