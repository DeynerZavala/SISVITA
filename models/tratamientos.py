from utils.db import db
from models.usuarios import Usuarios
from models.especialistas import Especialistas


class Tratamientos(db.Model):
    __tablename__ = 'Tratamientos'
    
    tratamiento_id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('Usuarios.usuario_id'), nullable=True)
    especialista_id = db.Column(db.Integer, db.ForeignKey('Especialistas.especialista_id'), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    plan = db.Column(db.Text, nullable=True)
    fecha_inicio = db.Column(db.Date, nullable=True)
    fecha_fin = db.Column(db.Date, nullable=True)

    def __init__(self, tratamiento_id, usuario_id, especialista_id, descripcion, plan, fecha_inicio, fecha_fin):
        self.tratamiento_id = tratamiento_id
        self.usuario_id = usuario_id
        self.especialista_id = especialista_id
        self.descripcion = descripcion
        self.plan = plan
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin