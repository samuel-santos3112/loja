from daoTeste import Session
from models import Cliente


session = Session()

cliente = Cliente('Samuel',1.71,'31-12-1998')
cliente2 = Cliente('Marcos',1.67,'05-02-2008')

session.add(cliente)
session.commit()
session.close()