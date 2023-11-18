#!/usr/bin/python3
"""Write a script that prints the first State object from the
database hbtn_0e_6_usa"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from sqlalchemy.engine.url import URL


if __name__ == "__main__":
    db = {'drivername': 'mysql+mysqldb',
          'host': 'localhost',
          'port': '3306',
          'username': sys.argv[1],
          'password': sys.argv[2],
          'database': sys.argv[3]}
    url = URL.create(**db)
    engine = create_engine(url, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        states_with_a = (
                session.query(State)
                .filter(State.name.like('%a%'))
                .order_by(State.id)
                .all()
                )
        if states_with_a:
            for state in states_with_a:
                print("{}: {}".format(state.id, state.name))
            else:
                print("Nothing")
            session.close()
