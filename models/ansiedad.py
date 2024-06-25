from utils.db import db


class Ansiedad(db.Model):
    __tablename__ = 'ansiedad'

    ansiedad_id = db.Column(db.Integer, primary_key=True)
    nivel = db.Column(db.String(255))
    
    def __init__(self, nivel):
        self.nivel = nivel
        