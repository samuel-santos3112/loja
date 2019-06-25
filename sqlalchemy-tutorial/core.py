from datetime import datetime
from sqlalchemy import create_engine
from pprint import pprint
from sqlalchemy import select
from metadata import MetaData

                      

engine = create_engine('postgresql://postgres:psql@localhost:5432/sqlalchemy')

metadata = MetaData(bind=engine)

words_table = Table('clientes', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('nome', String(40), index=True),
                    Column('altura', Float, nullable=False),
                    Column('data_nascimento', Date))
                 
metadata.create_all()
