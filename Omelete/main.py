from flask import *
import shutil
from modelo import *
#from persistencia import *
import os
app = Flask(__name__)
servidor = os.getcwd()
servidor = servidor.replace("\\","/")
app.config['UPLOAD_FOLDER'] = servidor + '/static/arquivos/'
diretorio = servidor + '/static/arquivos/'
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

if __name__ == '__main__':
	app.run(debug=True)