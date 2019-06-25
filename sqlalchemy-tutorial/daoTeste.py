# coding=utf-8

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData
from datetime import date



engine = create_engine('postgresql://postgres:psql@localhost:5432/loja')
Session = sessionmaker(bind=engine)

Base = declarative_base()
metadata = Base.metadata






