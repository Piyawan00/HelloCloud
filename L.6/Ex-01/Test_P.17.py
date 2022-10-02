import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User

engine = create_engine('sqlite:///user.db', echo=False)

# Base.metadata.drop_all(engine) #
Base.metadata.drop_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

user1 = User(name='User1', fullname='Ed Jones', nickname='ed')
#user2 = User(name='User2', fullname='TEd Jones', nickname='Ted')
#user3 = User(name='User3', fullname='STEd Jones', nickname='STed')
#user4 = User(name='User4', fullname='WTEd Jones', nickname='WTed')


session.add(user1)
session.commit()