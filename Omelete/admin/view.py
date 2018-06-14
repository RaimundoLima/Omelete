from flask import *

mod=Blueprint('admin',__name__,template_folder='templates')

@mod.route('/')
def index():
	return render_template('admin/index.html')