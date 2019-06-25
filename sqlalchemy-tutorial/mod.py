# coding: utf-8
from sqlalchemy import Column, Date, Integer, Numeric, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Cliente(Base):
    __tablename__ = 'cliente'

    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    altura = Column(Numeric(4, 2))
    data_nascimento = Column(Date)

    def __init__(self,nome,altura,data_nascimento):
        self.nome = nome
        self.altura = altura
        self.data_nascimento = data_nascimento