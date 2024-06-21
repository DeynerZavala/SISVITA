from utils.db import db


class Opciones_predeterminadas(db.Model):
    __tablename__ = 'opciones_predeterminadas'

    op_pre_id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)

    
    def __init__(self, opcion_pre_id, nombre):
        self.opcion_pre_id = opcion_pre_id
        self.nombre = nombre
