from utils.db import db


class Respuestas(db.Model):
    __tablename__ = 'respuesta'

    respuesta_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    opcion_id = db.Column(db.Integer, db.ForeignKey('opciones.opcion_id'))
    res_user_id = db.Column(db.Integer, db.ForeignKey('respuesta_usuario.res_user_id'))

    def __init__(self, opcion_id, res_user_id):
        self.opcion_id = opcion_id
        self.res_user_id = res_user_id
