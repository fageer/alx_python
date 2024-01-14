from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1],
                                                                   argv[2],
                                                                   argv[3]))

Session = sessionmaker(bind=engine)

session = Session()
Base.metadata.create_all(engine)

states = session.query(State).order_by(State.id).all()
for state in states:
    print(state.id, state.name)

session.close()
