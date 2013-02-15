from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for

from app import db
from app.gallery.models import Album

mod = Blueprint('gallery', __name__, url_prefix='/gallery')

@mod.route('/')
def home():
	return render_template("gallery/main.html")
