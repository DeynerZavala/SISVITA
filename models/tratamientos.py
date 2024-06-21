from utils.db import db
from models.usuarios import Usuarios
from models.especialistas import Especialistas


class Tratamientos(db.Model):
    __tablename__ = 'tratamientos'
    
    tratamiento_id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.usuario_id'), nullable=True)
    especialista_id = db.Column(db.Integer, db.ForeignKey('especialistas.especialista_id'), nullable=False)
    tratamiento_nombre = db.Column(db.String(255))
    descripcion = db.Column(db.Text, nullable=True)
    fecha_inicio = db.Column(db.TIMESTAMP(timezone=True), nullable=False)
    fecha_fin = db.Column(db.TIMESTAMP(timezone=True), nullable=False)

    def __init__(self, tratamiento_id, usuario_id, especialista_id, tratamiento_nombre, descripcion, fecha_inicio, fecha_fin):
        self.tratamiento_id = tratamiento_id
        self.usuario_id = usuario_id
        self.especialista_id = especialista_id
        self.tratamiento_nombre = tratamiento_nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin