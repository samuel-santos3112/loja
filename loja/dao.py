import psycopg2
from model import Cliente

SQL_DELETE = 'delete from cliente where id=%s'
SQL_UNACCENT = 'create extension unaccent'
SQL_SELECT_NOME = 'SELECT * FROM cliente WHERE nome =%s'
SQL_SELECT_ID = 'SELECT * FROM cliente WHERE id =%s'
SQL_SELECT_ALL = 'select * from cliente order by id'
SQL_UPDATE = 'update cliente set nome=%s, altura=%s, data_nascimento=%s where id =%s'
SQL_CREATE = 'INSERT INTO cliente (nome, altura, data_nascimento) values (%s,%s,%s)'

connection = psycopg2.connect(user="postgres",
                              password="psql",
                              host="127.0.0.1",
                              port="5432",
                              database="loja")

cursor = connection.cursor()


def criar(Cliente):
    cursor.execute(SQL_CREATE, (Cliente.nome, Cliente.altura, Cliente.data_nascimento))
    Cliente.id = cursor.lastrowid
    connection.commit()
    return Cliente

def atualizar(Cliente):
        cursor.execute(SQL_UPDATE, (Cliente.nome, Cliente.altura, Cliente.data_nascimento,Cliente.id))
        connection.commit()
        return Cliente

def listar():
        cursor.execute(SQL_SELECT_ALL)
        clientes = cursor.fetchall()
        def cria_cliente(tupla):
                return Cliente(tupla[0],tupla[1],tupla[2],tupla[3])
        listmap = list(map(cria_cliente, clientes))
        return listmap
         
def listar_por_nome(nome):
    cursor.execute(SQL_SELECT_NOME, (nome,))
    cliente = cursor.fetchone()
    return Cliente(cliente[0],cliente[1],cliente[2],cliente[3])  

def listar_por_id(id):
    cursor.execute(SQL_SELECT_ID, (id,))
    cliente = cursor.fetchone()
    return Cliente(cliente[0],cliente[1],cliente[2],cliente[3])        

def deletar_por_id(id):
    cursor.execute(SQL_DELETE, (id,))
    connection.commit()
