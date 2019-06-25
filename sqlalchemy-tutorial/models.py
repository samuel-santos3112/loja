# coding: utf-8
from sqlalchemy import Column, Date, Integer, Numeric, String, text
from sqlalchemy.ext.declarative import declarative_base
from daoTeste import Base


class Cliente(Base):
    __tablename__ = 'cliente'

    id = Column(Integer, primary_key=True, server_default=text("nextval('cliente_id_seq'::regclass)"))
    nome = Column(String(50), nullable=False)
    altura = Column(Numeric(4, 2), nullable=False)
    data_nascimento = Column(Date, nullable=False)

    def __init__(self,nome,altura,data_nascimento):
        self.nome = nome
        self.altura = altura
        self.data_nascimento = data_nascimento


class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(String(8), primary_key=True)
    nome = Column(String(20), nullable=False)
    senha = Column(String(20), nullable=False)

    def __init__ (self, nome, senha):
        self.nome = nome 
        self.senha = senha

