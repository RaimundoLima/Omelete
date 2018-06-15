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
app.register_blueprint(admin.view.admin, url_prefix='/admin')
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
##############NOTICIAAA
@app.route("/noticia")
def noticia():
	noticiaDAO = NoticiasDAO()
	return render_template("noticia.html",noticiaLista=noticiaDAO.listar())

@app.route("/noticia/<id>")
def obterNoticia(id):
	pessoaDAO = PessoaDAO()
	noticiasDAO = NoticiasDAO()
	comentarioDAO = ComentarioDAO()
	pessoa=pessoaDAO.login(session['login'],session['senha'])
	return render_template("noticia.html",noticias=noticiaDAO.obter(id),comentarios=comentarioDAO.listar(),pessoa=pessoa)

@app.route("/noticia/comentando",methods=['POST'])
def adicionarComentario(): 
	if session is not None:
		idNoticia = request.form['idNoticia']
		idPessoa = request.form['idPessoa']
		texto = request.form['texto']
		dataComentario = request.form['dataComentario']
		noticiasDAO = NoticiasDAO()
		comentarioDAO = ComentarioDAO()
		return render_template("noticia.html",noticias=noticiaDAO.obter(id),comentarios=comentarioDAO.listar())

@app.route("/noticia/comentario/editar/<idComentario>")
def editarComentario(idComentario): 
	pessoaDAO = PessoaDAO()
	pessoa = pessoaDAO.login(session['login'],session['senha']) 
	comentarioDAO = ComentarioDAO()
	comentario = comentarioDAO.obter(idComentario)
	if (comentario.idpessoa == pessoa.id):
		return render_template("adicionarComentario.html")

@app.route("/noticia/comentario/editando/", methods=['POST'])
def editandoComentario(): 
	comentarioDAO = ComentarioDAO()
	idNoticia = request.form['idNoticia']
	idPessoa = request.form['idPessoa']
	texto = request.form['texto']
	dataComentario = request.form['dataComentario']
	id = request.form['id']
	comentarioDAO.alterar(Comentario(idNoticia, idPessoa, texto, dataComentario))
	redirect(url_for('noticia'))

@app.route("/noticia/comentario/excluir/<idComentario>")
def excluirComentario(idComentario): 
	pessoaDAO = PessoaDAO()
	pessoa = pessoaDAO.login(session['login'],session['senha']) 
	comentarioDAO = ComentarioDAO()
	comentario = comentarioDAO.obter(idComentario)
	if (comentario.idpessoa == pessoa.id):
		comentarioDAO.excluir(id)
		redirect(url_for('noticia'))

###################PESSOA
@app.route("/pessoa/")
def cadastro():
	return render_template('edit-pessoa.html',pessoa=[],acao='cadastro')

@app.route("/pessoa/cadastrando", methods=['POST'])
def cadastrarPessoa():
	pessoaDAO = PessoaDAO()
	login = request.form['login']
	senha = request.form['senha']
	nome =  request.form['nome']
	#tipo = request.form['tipo']
	usuario=pessoaDAO.login(login,senha)
	if usuario is None:
		pessoa = Pessoa(login, senha, nome)#, tipo)
		pessoaDAO.adicionar(pessoa)
		redirect(url_for('/'))

@app.route("/pessoa/editar")
def editarPessoa():
	pessoaDAO = PessoaDAO()
	pessoa = pessoaDAO.login(session['login'], session['senha'])
	return render_template('edit-pessoa.html', pessoa=pessoa,acao='editando')

@app.route("/pessoa/editando/", methods=['POST'])
def editandoPessoa():
	pessoaDAO = PessoaDAO()
	login = request.form['login']
	senha = request.form['senha']
	nome = request.form['nome']
	#tipo = request.form['tipo']
	id = request.form['id']
	pessoaDAO.alterar(Pessoa(login,senha,nome,tipo,id))
	redirect(url_for('pessoa'))

if __name__ == '__main__':
	app.run(debug=True)