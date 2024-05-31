from utils.db import db


class Tests(db.Model):
    __tablename__ = 'tests'
    
    test_id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.Text, nullable=True)
    fecha_creacion = db.Column(db.Date, nullable=True)

    def __init__(self, test_id, descripcion, fecha_creacion):
        self.test_id = test_id
        self.descripcion = descripcion
        self.fecha_creacion = fecha_creacion