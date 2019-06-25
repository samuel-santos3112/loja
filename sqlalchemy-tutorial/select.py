from daoTeste import Session
from models import Cliente

session = Session()

clientes = session.query(Cliente).all()

for cliente in clientes:
    print(cliente)