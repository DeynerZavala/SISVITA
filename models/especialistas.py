from sqlalchemy import func

from utils.db import db


class Especialistas(db.Model):
    __tablename__ = 'especialistas'
    especialista_id = db.Column(db.Integer(), primary_key=True)
    nombre = db.Column(db.String(255))
    apellido_paterno = db.Column(db.String(255))
    apellido_materno = db.Column(db.String(255))
    titulo_id = db.Column(db.Integer())
    correo_electronico = db.Column(db.String(255))
    contrasena = db.Column(db.String(255))
    fecha_registro = db.Column(db.TIMESTAMP(timezone=True), nullable=True, default=func.now())
    ubigeo = db.Column(db.Integer())

    def __init__(self, nombre, apellido_paterno,
                 apellido_materno, titulo_id, correo_electronico,
                 contrasena, fecha_registro, ubigeo):
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.titulo_id = titulo_id
        self.correo_electronico = correo_electronico
        self.contrasena = contrasena
        self.fecha_registo = fecha_registro
        self.ubigeo = ubigeo

