from sqlalchemy import func
from utils.db import db


class Diagnostico(db.Model):
    __tablename__ = 'diagnostico'

    diagnostico_id = db.Column(db.Integer, primary_key=True)
    especialista_id= db.Column(db.Integer, db.ForeignKey('especialistas.especialista_id'), nullable=False)
    ansiedad_id= db.Column(db.Integer, db.ForeignKey('ansiedad.ansiedad_id'), nullable=False)
    fecha = db.Column(db.TIMESTAMP(timezone=True), nullable=False, default=func.now())
    observaciones = db.Column(db.Text)
    solicitar_cita = db.Column(db.Boolean)


    def __init__(self, especialista_id, ansiedad_id, fecha,
                 observaciones, solicitar_cita):
        self.especialista_id = especialista_id
        self.ansiedad_id = ansiedad_id
        self.fecha = fecha
        self.observaciones = observaciones
        self.solicitar_cita = solicitar_cita
