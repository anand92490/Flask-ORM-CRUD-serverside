from sqlalchemy import create_engine
engine = create_engine('sqlite:///school.db', echo = True)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
from models import *
Base.metadata.create_all(engine)