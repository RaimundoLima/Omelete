import psycopg2
from modelo import *
class Conexao:
	def abrir(self):
		self.conexao = psycopg2.connect("dbname=Trab2Ds2 user=postgres password=postgres host=localhost port=5433")
		self.cursor = self.conexao.cursor()

	def encerrar(self):
		self.conexao.close()
		self.cursor.close()
		
class PessoaDAO:
	def adicionar(self, pessoa):
		conexaoObj = Conexao()
		conexaoObj.abrir()
		conexaoObj.cursor.execute("insert into aluno (id, login, senha, nome, tipo) values(%s, %s, %s, %s, %s)", [pessoa.id, pessoa.login, pessoa.senha, pessoa.nome, pessoa.tipo])
		conexaoObj.conexao.commit()
		conexaoObj.encerrar()

	def listar(self):
		conexao = Conexao()
		conexao.abrir()
		conexao.cursor.execute("select * from pessoa")
		vet = conexao.cursor.fetchall()
		vetPessoa = []
		vetPessoa.append(Pessoa(vet[1],vet[2],vet[3],vet[4],vet[0]))
		conexao.encerrar()
		return vetPessoa

	def obter(self, id):
		conexao = Conexao()
		conexao.abrir()
		conexao.cursor.execute("select * from aluno where id=%s", [id])
		vet = conexao.cursor.fetchone()
		conexao.encerrar()
		vetPessoa = []
		vetPessoa.append(Pessoa(vet[1], vet[2], vet[3],vet[4],vet[0]))
		return vetPessoa
	def login(self, login, senha):
		conexao = Conexao()
		conexao.abrir()
		conexao.cursor.execute("select * from pessoa where login=%s and senha=%s", [login, senha])
		vet = conexao.cursor.fetchone()
		vetPessoa = []
		vetPessoa.append(Pessoa(vet[1], vet[2], vet[3],vet[4],vet[0]))
		conexao.encerrar()
		return aluno
	def alterar(self, pessoa):
		conexaoObj = Conexao()
		conexaoObj.abrir()
		conexaoObj.cursor.execute("update pessoa set login=%s, senha=%s, nome=%s, tipo=%s where id=%s", [aluno.login, aluno.senha, aluno.nome, aluno.tipo, aluno.id])
		conexaoObj.conexao.commit()
		conexaoObj.encerrar()

	def excluir(self, id):
		conexaoObj = Conexao()
		conexaoObj.abrir()
		conexaoObj.cursor.execute("delete from pessoa where id=%s", [id])
		conexaoObj.conexao.commit()
		conexaoObj.encerrar()
class AssuntoDAO:
	def adicionar(self, assunto):
		conexaoObj = Conexao()
		conexaoObj.abrir()
		conexaoObj.cursor.execute("insert into aluno (id, nome) values(%s, %s)", [pessoa.id, pessoa.nome])
		conexaoObj.conexao.commit()
		conexaoObj.encerrar()

	def listar(self):
		conexao = Conexao()
		conexao.abrir()
		conexao.cursor.execute("select * from assunto")
		vet = conexao.cursor.fetchall()
		vetAssunto = []
		vetAssunto.append(Assunto(vet[1],vet[0]))
		conexao.encerrar()
		return vetAssunto

	def obter(self, id):
		conexao = Conexao()
		conexao.abrir()
		conexao.cursor.execute("select * from assunto where id=%s", [id])
		vet = conexao.cursor.fetchone()
		conexao.encerrar()
		vetAssunto = []
		vetAssunto.append(Assunto(vet[1], vet[0]))
		return vetAssunto

	def alterar(self, assunto):
		conexaoObj = Conexao()
		conexaoObj.abrir()
		conexaoObj.cursor.execute("update assunto set nome=%s where id=%s", [assunto.nome, assunto.id])
		conexaoObj.conexao.commit()
		conexaoObj.encerrar()

	def excluir(self, id):
		conexaoObj = Conexao()
		conexaoObj.abrir()
		conexaoObj.cursor.execute("delete from assunto where id=%s", [id])
		conexaoObj.conexao.commit()
		conexaoObj.encerrar()
class NoticiaDAO:
	def adicionar(self, noticia):
		conexaoObj = Conexao()
		conexaoObj.abrir()
		conexaoObj.cursor.execute("insert into aluno (id, idassunto, titulo, texto, datapublicacao) values(%s, %s, %s, %s, %s)", [noticia.id, noticia.idassunto, noticia.titulo, noticia.texto, noticia.datapublicacao])
		conexaoObj.conexao.commit()
		conexaoObj.encerrar()

	def listar(self):
		conexao = Conexao()
		conexao.abrir()
		conexao.cursor.execute("select * from noticia")
		vet = conexao.cursor.fetchall()
		vetNoticia = []
		vetNoticia.append(Noticia(vet[1],vet[2],vet[3],vet[4],vet[0]))
		conexao.encerrar()
		return vetNoticia

	def obter(self, id):
		conexao = Conexao()
		conexao.abrir()
		conexao.cursor.execute("select * from noticia where id=%s", [id])
		vet = conexao.cursor.fetchone()
		conexao.encerrar()
		vetNoticia = []
		vetNoticia.append(Noticia(vet[1], vet[2], vet[3],vet[4],vet[0]))
		return vetNoticia
	def alterar(self, noticia):
		conexaoObj = Conexao()
		conexaoObj.abrir()
		conexaoObj.cursor.execute("update noticia set idassunto=%s, titulo=%s, texto=%s, datapublicacao=%s where id=%s", [noticia.idassunto, noticia.titulo, noticia.texto, noticia.datapublicacao, aluno.id])
		conexaoObj.conexao.commit()
		conexaoObj.encerrar()

	def excluir(self, id):
		conexaoObj = Conexao()
		conexaoObj.abrir()
		conexaoObj.cursor.execute("delete from noticia where id=%s", [id])
		conexaoObj.conexao.commit()
		conexaoObj.encerrar()
class Comentario:
	def adicionar(self, comentario):
		conexaoObj = Conexao()
		conexaoObj.abrir()
		conexaoObj.cursor.execute("insert into comentario (id, idnoticia, idpessoa, texto, datacomentario) values(%s, %s, %s, %s, %s)", [comentario.id, comentario.idnoticia, comentario.idpessoa, comentario.texto, comentario.datacomentario])
		conexaoObj.conexao.commit()
		conexaoObj.encerrar()

	def listar(self):
		conexao = Conexao()
		conexao.abrir()
		conexao.cursor.execute("select * from comentario")
		vet = conexao.cursor.fetchall()
		vetComentario = []
		vetComentario.append(Comentario(vet[1],vet[2],vet[3],vet[4],vet[0]))
		conexao.encerrar()
		return vetComentario

	def obter(self, id):
		conexao = Conexao()
		conexao.abrir()
		conexao.cursor.execute("select * from comentario where id=%s", [id])
		vet = conexao.cursor.fetchone()
		conexao.encerrar()
		vetComentario = []
		vetComentario.append(Noticia(vet[1], vet[2], vet[3],vet[4],vet[0]))
		return vetComentario
	def alterar(self, comentario):
		conexaoObj = Conexao()
		conexaoObj.abrir()
		conexaoObj.cursor.execute("update comentario set idnoticia=%s, idpessoa=%s, texto=%s, datacomentario=%s where id=%s", [comentario.idnoticia, comentario.idpessoa, comentario.texto, comentario.datacomentario, comentario.id])
		conexaoObj.conexao.commit()
		conexaoObj.encerrar()

	def excluir(self, id):
		conexaoObj = Conexao()
		conexaoObj.abrir()
		conexaoObj.cursor.execute("delete from comentario where id=%s", [id])
		conexaoObj.conexao.commit()
		conexaoObj.encerrar()