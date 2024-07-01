from utils.db import db


class Ansiedad_Semaforo(db.Model):
    __tablename__ = 'ansiedad_semaforo'

    ans_sem_id = db.Column(db.Integer, primary_key=True)
    semaforo = db.Column(db.Integer)

    def __init__(self, semaforo):
        self.semaforo = semaforo
