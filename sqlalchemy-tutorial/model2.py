# coding=utf-8

from sqlalchemy import Column, String, Integer, Date, Table, Float
from daoTeste import Base

class Cliente(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    altura = Column(Float)
    data_nascimento = Column(Date)

    def __init__(self,id,nome,altura,data_nascimento):
        self.id = id
        self.nome = nome
        self.altura = altura
        self.data_nascimento = data_nascimento

Base.create_all()