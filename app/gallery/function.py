from app.gallery.models import *

def get_all_album():
	return Album.query.all()