from utils.db import db


class Titulos(db.Model):
    __tablename__ = 'titulo'

    titulo_id = db.Column(db.Integer, primary_key=True)
    titulo_name = db.Column(db.String(255))


    def __init__(self, titulo_id, titulo_name):
        self.titulo_id = titulo_id
        self.titulo_name= titulo_name
