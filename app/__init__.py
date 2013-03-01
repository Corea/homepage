# -*- encoding: utf-8 -*- 
from flask import Flask, render_template
from flask import g, request, redirect, url_for
from flask.ext.sqlalchemy import SQLAlchemy
from functools import wraps

import function

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

def login_required(f):
	@wraps(f)
	def decorated_function(*args, **kwargs):
		if g.user is None:
			return redirect(url_for('login', next=request.url))
		return f(*args, **kwargs)
	return decorated_function


@app.route("/")
def main():
	lst = function.get_file_list()
	return render_template('main.html', lst=lst)

from app.gallery.views import mod as galleryModule
from app.god.views import mod as godModule

app.register_blueprint(galleryModule)
app.register_blueprint(godModule)


