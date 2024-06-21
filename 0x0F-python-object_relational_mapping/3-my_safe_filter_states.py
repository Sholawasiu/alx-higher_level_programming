#!/usr/bin/python3
"""
This script takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!
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
    state_name = sys.argv[4]

    cursor = database.cursor()
    query = "SELECT * FROM states WHERE BINARY states.name=%s"
    cursor.execute(query, (state_name,))

    for state in cursor.fetchall():
        print(state)

    cursor.close()
    database.close()


if __name__ == '__main__':
    main()
