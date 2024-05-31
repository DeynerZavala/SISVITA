from utils.db import db


class Usuarios(db.Model):
    __tablename__ = 'usuarios'

    usuario_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100))
    apellido_paterno = db.Column(db.String(100))
    apellido_materno = db.Column(db.String(100))
    correo_electronico = db.Column(db.String(100), unique=True)
    contrasena = db.Column(db.String(255))
    fecha_registro = db.Column(db.Date)

    def __init__(self,  nombre, apellido_paterno, apellido_materno,
                 correo_electronico, contrasena, fecha_registro):
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.correo_electronico = correo_electronico
        self.contrasena = contrasena
        self.fecha_registro = fecha_registro
