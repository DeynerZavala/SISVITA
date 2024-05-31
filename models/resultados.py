from utils.db import db
from models.tests import Tests
from models.usuarios import Usuarios
from models.especialistas import Especialistas



class Resultados(db.Model):
    __tablename__ = 'Resultados'
    
    resultado_id = db.Column(db.Integer, primary_key=True)
    test_id = db.Column(db.Integer, db.ForeignKey('Tests.test_id'), nullable=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('Usuarios.usuario_id'), nullable=True)
    especialista_id = db.Column(db.Integer, db.ForeignKey('Especialistas.especialista_id'), nullable=False)
    fecha = db.Column(db.Date, nullable=True)
    puntuacion = db.Column(db.Integer, nullable=True)
    interpretacion = db.Column(db.Integer, nullable=True)

    def __init__(self, resultado_id, test_id, usuario_id, especialista_id, fecha, puntuacion, interpretacion):
        self.resultado_id = resultado_id
        self.test_id = test_id
        self.usuario_id = usuario_id
        self.especialista_id = especialista_id
        self.fecha = fecha
        self.puntuacion = puntuacion
        self.interpretacion = interpretacion