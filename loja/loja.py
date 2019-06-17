from flask import Flask, render_template, request, redirect,url_for,flash
from model import Cliente
import dao

app = Flask(__name__)
app.secret_key = 'loja'


@app.route('/')
def index():
        lista = dao.listar()
        return render_template('lista.html', clientes = lista )


@app.route('/novo')
def novo():
    return render_template('novo.html')
   
    
@app.route('/criar',methods=['POST',])
def criar():
        nome = request.form['nome']
        altura = request.form['altura']
        data_nascimento = request.form['data_nascimento']
        cliente = Cliente(id,nome,altura,data_nascimento)
        dao.criar(cliente)
        flash('Criado com sucesso!')
        return redirect(url_for('index'))


@app.route('/editar/<int:id>')
def editar(id):
        lista = dao.listar()
        cliente = dao.listar_por_id(id)
        return render_template('editar.html', titulo='Editando Cliente', cliente = cliente,clientes = lista)
        

@app.route ('/atualizar',methods=['POST',])
def atualizar():
        id = request.form['id']
        nome = request.form['nome']
        altura = request.form['altura']
        data_nascimento = request.form['data_nascimento']
        cliente = Cliente(id,nome,altura,data_nascimento)
        dao.atualizar(cliente)
        flash('Cliente atualizado com sucesso!')
        return redirect(url_for('index'))

@app.route('/deletar/<int:id>')
def deletar(id):
        dao.deletar_por_id(id)
        flash('Cliente removido com sucesso!')
        return redirect(url_for('index'))

@app.route('/buscaNome', methods=['POST',])
def buscaNome():
        nome = request.form['pesquisarNome']
        lista = [dao.listar_por_nome(nome),]
        return render_template('lista.html', clientes = lista)


app.run(debug=True)


