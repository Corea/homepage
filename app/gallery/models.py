from app import db 
from datetime import datetime

class Album(db.Model):
	__tablename__ = 'picutres_album'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), nullable=False)
	created_time = db.Column(db.DateTime, nullable=False)
	updated_time = db.Column(db.DateTime, nullable=False)

	def __init__(self, name):
		name = name
		created_time = datetime.utcnow()
		updated_time = datetime.utcnow()

	def __repr__(self):
		return '<Album %s: %s>' % (self.id, self.name)
