# coding=utf-8

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import date


engine = create_engine('postgresql://postgres:psql@localhost:5432/sqlalchemy')

Session = sessionmaker(bind=engine)

Base = declarative_base()




