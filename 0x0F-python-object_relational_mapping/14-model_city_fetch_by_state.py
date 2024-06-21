#!/usr/bin/python3
"""
This script prints all city objects from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def main():
    """ Main function. """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3], pool_pre_ping=True))
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    result = session.query(State, City).filter(State.id == City.state_id) \
        .order_by(City.id).all()

    for states, city in result:
        print(f"{states.name}: ({city.id}) {city.name}")

    session.close()


if __name__ == '__main__':
    main()
