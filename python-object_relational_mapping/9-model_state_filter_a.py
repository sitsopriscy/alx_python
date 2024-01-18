# Write a script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa

# Your script should take 3 arguments: mysql username, mysql password and database name
# You must use the module SQLAlchemy
# You must import State and Base from model_state - from model_state import Base, State
# Your script should connect to a MySQL server running on localhost at port 3306
# Results must be sorted in ascending order by states.id
# The results must be displayed as they are in the example below
# Your code should not be executed when imported


"""Lists all State objects that contain the letter a from the database hbtn_0e_6_usa
"""

if __name__ == "__main__":
    """importing from sys, model_state and sqlalchely"""
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    path = "mysql+mysqldb://{}:{}@localhost/{}"
    engine = create_engine(path.format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    for states in (
        session.query(State).filter(State.name.like("%a%")).order_by(State.id).all()
    ):
        print("{}: {}".format(states.id, states.name))

    session.close()
