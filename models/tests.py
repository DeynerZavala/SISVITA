from sqlalchemy import func

from utils.db import db


class Tests(db.Model):
    __tablename__ = 'tests'
    
    test_id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(255), nullable=True)
    descripcion = db.Column(db.Text, nullable=True)
    fecha_creacion = db.Column(db.TIMESTAMP(timezone=True), nullable=True, default=func.now())

    def __init__(self,titulo,descripcion, fecha_creacion, template_id):
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_creacion = fecha_creacion
        self.template_id = template_id