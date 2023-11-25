# app/models.py
from app import db

class Libro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(128), index=True, unique=True)

    def __repr__(self):
        return f'<Libro {self.titulo}>'
