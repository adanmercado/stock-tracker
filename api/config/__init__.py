import os

from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

db_basedir = os.path.abspath(os.path.curdir)
db_filename = 'database.db'
SQLALCHEMY_DATABASE_URI = f'sqlite:///{db_basedir}/{db_filename}'

engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)

Session = sessionmaker(bind=engine)

SqlAlchemyBaseModel = declarative_base()
