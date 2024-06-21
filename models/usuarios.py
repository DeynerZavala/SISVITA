from sqlalchemy import func
from utils.db import db


class Usuarios(db.Model):
    __tablename__ = 'usuarios'

    usuario_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(255))
    correo_electronico = db.Column(db.String(255), unique=True)
    contrasena = db.Column(db.String(255))
    fecha_registro = db.Column(db.TIMESTAMP(timezone=True), nullable=True, default=func.now())
    apellido_paterno = db.Column(db.String(255))
    apellido_materno = db.Column(db.String(255))
    ubigeo = db.Column(db.Integer)

    def __init__(self, nombre, apellido_paterno, apellido_materno,
                 correo_electronico, contrasena, fecha_registro, ubigeo):
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.correo_electronico = correo_electronico
        self.contrasena = contrasena
        self.fecha_registro = fecha_registro
        self.ubigeo = ubigeo