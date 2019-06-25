from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:psql@localhost:5432/loja2'

db = SQLAlchemy(app)
class Clientes (db.Model):
    id = db.Column(db.Integer,primary_key = True)
    nome = db.Column(db.String(50))
    altura = db.Column(db.Float)
    data_nascimento = db.Column(db.Date)

    def __init__(self,nome,altura,data_nascimento):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.altura = altura

db.create_all()
