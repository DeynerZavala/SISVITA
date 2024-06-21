from utils.db import db
from models.especialistas import Especialistas


class Foros(db.Model):
    __tablename__ = 'foros'
    
    foro_id = db.Column(db.Integer, primary_key=True)
    especialista_id = db.Column(db.Integer, db.ForeignKey('especialistas.especialista_id'), nullable=False)
    tema = db.Column(db.String(255), nullable=True)
    descripcion = db.Column(db.Text, nullable=True)
    fecha_creacion = db.Column(db.TIMESTAMP(timezone=True), nullable=False)

    def __init__(self, foro_id, especialista_id, tema, descripcion, fecha_creacion):
        self.foro_id = foro_id
        self.especialista_id = especialista_id
        self.tema = tema
        self.descripcion = descripcion
        self.fecha_creacion = fecha_creacion