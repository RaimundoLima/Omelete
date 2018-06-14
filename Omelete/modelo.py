class Pessoa:
	def __init__(self, login, senha, nome, tipo, id):
		self.login = login
		self.senha = senha
		self.nome = nome
		self.tipo = tipo
		self.id = id
	def __repr__(self):
		return str(self.id) +";"+ self.login +";"+ self.senha +";"+ self.nome +";"+ self.tipo +";"+"\n"
class Assunto:
	def __init__(self, nome, id):
		self.nome = nome
		self.id = id
	def __repr__(self):
		return str(self.id) +";"+ self.nome +";"+"\n"
class Noticia:
	def __init__(self, idassunto, titulo, texto, datapublicacao, id):
		self.idassunto = idassunto
		self.titulo = titulo
		self.texto = texto
		self.datapublicacao = datapublicacao
		self.id = id
	def __repr__(self):
		return str(self.id) +";"+ str(self.idassunto) +";"+ self.titulo +";"+ self.texto +";"+ self.datapublicacao +";"+"\n"
class Comentario:
	def __init__(self, idnoticia, idpessoa, texto, datacomentario, id):
		self.idnoticia = idnoticia
		self.idpessoa = idpessoa
		self.texto = texto
		self.datacomentario = datacomentario
		self.id = id
	def __repr__(self):
		return str(self.id) +";"+ str(self.idnoticia) +";"+ str(self.idpessoa) +";"+ self.texto +";"+ self.datacomentario +";"+"\n"