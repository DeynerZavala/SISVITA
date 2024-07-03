from sqlalchemy import func
from utils.db import db


class Diagnostico(db.Model):
    __tablename__ = 'diagnostico'

    diagnostico_id = db.Column(db.Integer, primary_key=True)
    especialista_id= db.Column(db.Integer, db.ForeignKey('especialistas.especialista_id'), nullable=False)
    ansiedad_id= db.Column(db.Integer, db.ForeignKey('ansiedad.ansiedad_id'), nullable=False)
    fecha = db.Column(db.TIMESTAMP(timezone=True), nullable=False, default=func.now())
    comunicacion_estudiante = db.Column(db.Text)
    solicitar_cita = db.Column(db.Boolean)
    tratamiento_id = db.Column(db.Integer, nullable=False)
    fundamentacion_cientifica= db.Column(db.Text)


    def __init__(self, especialista_id, ansiedad_id, fecha,
                 comunicacion_estudiante, solicitar_cita,tratamiento_id, fundamentacion_cientifica):
        self.especialista_id = especialista_id
        self.ansiedad_id = ansiedad_id
        self.fecha = fecha
        self.comunicacion_estudiante = comunicacion_estudiante
        self.solicitar_cita = solicitar_cita
        self.tratamiento_id = tratamiento_id
        self.fundamentacion_cientifica=fundamentacion_cientifica
