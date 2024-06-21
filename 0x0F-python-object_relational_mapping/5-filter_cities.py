#!/usr/bin/python3
"""
This script takes in the name of a state as an argument and lists all cities of
that state, using the database hbtn_0e_4_usa.
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
        db=sys.argv[3],
    )

    cursor = database.cursor()
    cursor.execute("SELECT * FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                   ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`")

    print(", ".join([col[2] for col in cursor.fetchall() if col[4] ==
                     sys.argv[4]]))

    cursor.close()
    database.close()


if __name__ == '__main__':
    main()
