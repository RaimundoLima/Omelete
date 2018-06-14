from flask import *
import shutil
from modelo import *
#from persistencia import *
import os
app = Flask(__name__)
# para sessao
app.secret_key = "chave_secreta"
#a###########################Admin Blueprint
from admin.view import *
app.register_blueprint(admin.view.mod, url_prefix='/admin')
#
#############################################LISTA DE ERROS
@app.errorhandler(400)
def error400(error):
	flash("ERROR 400")
	return render_template("error.html")

@app.errorhandler(401)
def error401(error):
	flash("ERROR 401")
	return render_template("error.html")

@app.errorhandler(402)
def error402(error):
	flash("ERROR 402")
	return render_template("error.html")

@app.errorhandler(403)
def error403(error):
	flash("ERROR 403")
	return render_template("error.html")

@app.errorhandler(404)
def error404(error):
	flash("ERROR 404")
	return render_template("error.html")

@app.errorhandler(405)
def error405(error):
	flash("ERROR 405")
	return render_template("error.html")

@app.errorhandler(500)
def error500(error):
	flash("ERROR 500")
	return render_template("error.html")

@app.errorhandler(502)
def error502(error):
	flash("ERROR 502")
	return render_template("error.html")
#################################################################

@app.route("/")
def index(): 
	return render_template("index.html")

@app.route("/")
def login():
	return render_template("login.html")

@app.route("/deslogar")
def deslogar():
	session.pop('login', None)
	session.pop('senha', None)
	session.pop('tipo', None)
	return redirect(url_for("home"))

@app.route("/login", methods = ['POST'])
def logando():
	login = request.form['login']
	senha = request.form['senha']
	tipo = request.form['tipo']
	if (login == 'admin' and senha == 'admin'):
		session['login'] = login
		session['senha'] = senha
		session['tipo'] = tipo
		return redirect(url_for("home"))
	pessoaDAO = PessoaDAO()
	pessoa=pessoaDAO.login(login,senha)

	if pessoa is not None :
		session['login'] = login
		session['senha'] = senha
		session['tipo'] = tipo
		return redirect(url_for("home"))
	else:
		return render_template("erro.html", mensagem = "login invalido...")

@app.route("/home")
def home(): 
	return render_template("index.html")

@app.route("/noticia")
def noticia():
	noticiaDAO = NoticiasDAO()
	return render_template("noticia.html",noticiaLista=noticiaDAO.listar())

@app.route("/noticia/<id>")
def obterNoticia(id):
	noticiasDAO = NoticiasDAO()
	comentarioDAO = ComentarioDAO()
	pessoa=pessoaDAO.login(session['login'],session['senha'])
	return render_template("noticia.html",noticiaLista=noticiaDAO.obter(id),comentarioLista=comentarioDAO.listar(),pessoa=pessoa)

@app.route("/noticia/",methods=['POST'])
def comentar(): 
	if session is not None:
		idNoticia = request.form['idNoticia']
		idPessoa = request.form['idPessoa']
		texto = request.form['texto']
		dataComentario = request.form['dataComentario']
		noticiasDAO = NoticiasDAO()
		comentarioDAO = ComentarioDAO()
		return render_template("noticia.html",noticiaLista=noticiaDAO.obter(id),comentarioLista=comentarioDAO.listar())

@app.route("/cadastrar/")
def cadastro():
	return render_template('cadastrar.html')

@app.route("/cadastrar/cadastrando", methods=['POST'])
def cadastrarPessoa():
	pessoaDAO = PessoaDAO()
	login = request.form['login']
	senha = request.form['senha']
	nome =  request.form['nome']
	tipo = request.form['tipo']
	usuario=pessoaDAO.login(login,senha)
	if usuario is None:
		pessoa = Pessoa(login, senha, nome, tipo)
		pessoaDAO.adicionar(pessoa)
		redirect(url_for('home'))

@app.route("/meusdados/")
def cadast():
	return render_template('cadastrar.html')

if __name__ == '__main__':
	app.run(debug=True)
