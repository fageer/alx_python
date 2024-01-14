from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1],
                                                                   argv[2],
                                                                   argv[3]))

Session = sessionmaker()

session = Session(bind=engine)
Base.metadata.create_all(engine)

state = session.query(State).order_by(State.id).first()

if state:
    print("{}: {}".format(state.id, state.name))
else:
    print("Nothing")

session.close()
