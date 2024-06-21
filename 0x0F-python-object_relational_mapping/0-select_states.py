#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa.
"""
import sys
import MySQLdb


def main():
    """
    Main function
    """
    database = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = database.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id")

    for state in cursor.fetchall():
        print(state)

    cursor.close()
    database.close()


if __name__ == "__main__":
    main()
