from utils.db import db
from models.usuarios import Usuarios
from models.especialistas import Especialistas


class Tratamientos(db.Model):
    __tablename__ = 'tratamientos'
    
    tratamiento_id = db.Column(db.Integer, primary_key=True)
    tratamiento_nombre = db.Column(db.String(255))

    def __init__(self, tratamiento_id,  tratamiento_nombre):
        self.tratamiento_nombre = tratamiento_nombre
