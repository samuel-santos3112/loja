# coding: utf-8
from sqlalchemy import Column, Date, Integer, Numeric, String, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Cliente(Base):
    __tablename__ = 'cliente'

    id = Column(Integer, primary_key=True, server_default=text("nextval('cliente_id_seq'::regclass)"))
    nome = Column(String(50))
    altura = Column(Numeric(4, 2))
    data_nascimento = Column(Date)
