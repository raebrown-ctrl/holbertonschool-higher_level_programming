#!/usr/bin/python3
"""
lists all states with name from the database
"""
import MySQLdb
from sys import argv


def main(username, passwd, db, statename):
    """
    list  must be sarting with N (upper N)
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
    c.execute("""SELECT C.name
                FROM cities C
                INNER JOIN states S
                ON C.state_id = S.id
                WHERE S.name = %s
                ORDER BY C.id """, (statename, ))

    rows = c.fetchall()
    for i in range(len(rows)):
        if i + 1 < len(rows):
            print(rows[i][0], end=", ")
        else:
            print(rows[i][0], end="")
    print("")


if __name__ == '__main__':
    main(argv[1], argv[2], argv[3], argv[4])
