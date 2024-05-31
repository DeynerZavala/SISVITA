from utils.db import db



class Opciones(db.Model):
    __tablename__ = 'opciones'
    
    opcion_id = db.Column(db.Integer, primary_key=True)
    pregunta_id = db.Column(db.Integer, db.ForeignKey('Preguntas.pregunta_id'), nullable=True)
    op_pre_id = db.Column(db.Integer, db.ForeignKey('opciones_predeterminada.op_pre_id'), nullable=True)
    def __init__(self, opcion_id, pregunta_id, op_pre_id):
        self.opcion_id = opcion_id
        self.pregunta_id = pregunta_id
        self.op_pre_id = op_pre_id