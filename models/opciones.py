from utils.db import db
from models.preguntas import Preguntas



class Opciones(db.Model):
    __tablename__ = 'opciones'
    
    opcion_id = db.Column(db.Integer, primary_key=True)
    pregunta_id = db.Column(db.Integer, db.ForeignKey('Preguntas.pregunta_id'), nullable=True)
    textoopcion = db.Column(db.Text, nullable=True)
    escorrecta = db.Column(db.Boolean, nullable=True)

    def __init__(self, opcion_id, pregunta_id, textoopcion, escorrecta):
        self.opcion_id = opcion_id
        self.pregunta_id = pregunta_id
        self.textoopcion = textoopcion
        self.escorrecta = escorrecta