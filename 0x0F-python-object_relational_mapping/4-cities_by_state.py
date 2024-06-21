#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_4_usa.
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
    query = """SELECT cities.id, cities.name, states.name FROM states
    JOIN cities ON states.id=cities.state_id ORDER BY cities.id ASC"""
    cursor.execute(query)

    for city in cursor.fetchall():
        print(city)

    cursor.close()
    database.close()


if __name__ == '__main__':
    main()
