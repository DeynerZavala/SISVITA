from sqlalchemy import func

from utils.db import db


class Respuesta_Usuario(db.Model):
    __tablename__ = 'respuesta_usuario'

    usuario_id = db.Column(db.Integer, primary_key=True)
    respuesta_id = db.Column(db.Text, primary_key=True)
    resultado_id= db.Column(db.Text, nullable=True)
    fecha_fin = db.Column(db.TIMESTAMP(timezone=True), nullable=False, default=func.now())


    def __init__(self, usuario_id, respuesta_id, fecha_fin):
        self.usuario_id = usuario_id
        self.respuesta_id = respuesta_id
        self.fecha_fin = fecha_fin

