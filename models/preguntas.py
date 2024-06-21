from utils.db import db
from models.tests import Tests


class Preguntas(db.Model):
    __tablename__ = 'preguntas'
    
    pregunta_id = db.Column(db.Integer, primary_key=True)
    textopregunta = db.Column(db.Text, nullable=False)
    test_id = db.Column(db.Integer, db.ForeignKey('tests.test_id'))


    def __init__(self, pregunta_id, test_id, textopregunta):
        self.pregunta_id = pregunta_id
        self.test_id = test_id
        self.textopregunta = textopregunta