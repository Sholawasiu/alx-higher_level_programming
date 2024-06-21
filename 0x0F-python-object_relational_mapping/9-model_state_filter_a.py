#!/usr/bin/python3
# 9-model_state_filter_a.py
# Author: @tonybnya
"""
This script lists all State objects that contain the letter a from
the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """ Main function """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    result = session.query(State).filter(State.name.like('%a%')) \
        .order_by(State.id)

    for element in result:
        print(f"{element.id}: {element.name}")

    session.close()


if __name__ == '__main__':
    main()
