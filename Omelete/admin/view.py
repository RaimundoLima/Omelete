from flask import *

admin=Blueprint('admin',__name__,template_folder='templates',static_folder = 'static'))

@admin.route('/')
def index():
	return render_template('admin/index.html')