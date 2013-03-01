from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for

from app import db
from app.gallery import function

mod = Blueprint('gallery', __name__, url_prefix='/gallery')

@mod.route('/')
def home():
	album_list = function.get_all_album()
	return render_template("gallery/main.html", album_list=album_list)
