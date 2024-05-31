from utils.db import db


class Especialistas(db.Model):
    __tablename__ = 'especialistas'
    especialista_id = db.Column(db.Integer(), primary_key=True)
    nombre = db.Column(db.String(100))
    apellido_paterno = db.Column(db.String(100))
    apellido_materno = db.Column(db.String(100))
    titulo = db.Column(db.Integer(), db.ForeignKey('Titulos.titulo_id'))
    correo_electronico = db.Column(db.String(100))
    contrasena = db.Column(db.String(50))
    fecha_registro = db.Column(db.Date())

    def __init__(self, especialista_id, nombre, apellido_paterno,
                 apellido_materno, titulo, correo_electronico,
                 contrasena, fecha_registo):
        self.especialista_id = especialista_id
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.titulo = titulo
        self.correo_electronico = correo_electronico
        self.contrasena = contrasena
        self.fecha_registo = fecha_registo
