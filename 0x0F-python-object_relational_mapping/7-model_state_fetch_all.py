#!/usr/bin/python3
"""
This script lists all State objects from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """ Main function. """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()

    for i in session.query(State).order_by(State.id).all():
        print(f"{i.id}: {i.name}")

    session.close()


if __name__ == '__main__':
    main()
