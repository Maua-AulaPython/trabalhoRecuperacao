from mauaserver import db

class Testes(db.Model):
	id		= db.Column(db.Integer, primary_key=True)
	identificacao	= db.Column(db.String(100))
	movimentos	= db.Column(db.Integer)