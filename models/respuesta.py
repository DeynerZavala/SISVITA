from utils.db import db


class Respuestas(db.Model):
    __tablename__ = 'respuesta'

    respuesta_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pregunta_id = db.Column(db.Text, nullable=False)
    opcion_id = db.Column(db.Text, nullable=False)
    es_correcto = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, pregunta_id, opcion_id):
        self.pregunta_id = pregunta_id
        self.opcion_id = opcion_id

