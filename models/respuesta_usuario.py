from sqlalchemy import func

from utils.db import db


class Respuesta_Usuario(db.Model):
    __tablename__ = 'respuesta_usuario'

    res_user_id=db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.usuario_id'))
    diagnostico_id = db.Column(db.Integer, db.ForeignKey('diagnostico.diagnostico_id'))
    fecha_fin = db.Column(db.TIMESTAMP(timezone=True), nullable=False, default=func.now())
    puntuacion=db.Column(db.Integer)

    def __init__(self, res_user_id, usuario_id, diagnostico_id, fecha_fin, puntuacion):
        self.res_user_id = res_user_id
        self.usuario_id = usuario_id
        self.diagnostico_id = diagnostico_id
        self.fecha_fin = fecha_fin
        self.puntuacion = puntuacion


