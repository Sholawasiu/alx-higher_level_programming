#!/usr/bin/python3
"""
This script creates the State "California" with the City "San Francisco"
from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City


def main():
    """ Main function """
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()

    session.add(City(name="San Francisco", state=State(name="California")))

    session.commit()


if __name__ == '__main__':
    main()
