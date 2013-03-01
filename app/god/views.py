from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for

from app import settings

from app import db
from app.god import function
from app.god.forms import LoginForm
from app.god.decorators import requires_login

mod = Blueprint('god', __name__, url_prefix='/god')

@mod.route('/')
@requires_login
def home():
	return render_template("god/main.html")

@mod.before_request
def before_request():
	"""
	pull user's profile from the database before every request are treated
	"""
	g.god = None
	if settings.GOD_SESSION in session:
		g.god = True

@mod.route('/login/', methods=['GET', 'POST'])
def login():
	"""
	Login form
	"""
	form = LoginForm(request.form)
	# make sure data are valid, but doesn't validate password is right
	if form.validate_on_submit():
		if form.user_id.data == settings.GOD_ID and form.password.data == settings.GOD_PASSWORD:
			# the session can't be modified as it's signed, 
			# it's a safe place to store the user id
			session[settings.GOD_SESSION] = settings.GOD_ID
			return redirect(url_for('god.home'))
		flash('Wrong id or password', 'error-message')
	return render_template("god/login.html", form=form)

@mod.route('/logout/')
@requires_login
def logout():
	g.god = None
	del session[settings.GOD_SESSION]
	return redirect(url_for('main'))
