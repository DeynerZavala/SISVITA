from utils.db import db



class Citas(db.Model):
    __tablename__ = 'citas'
    #
    cita_id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.usuario_id'), nullable=False)
    especialista_id = db.Column(db.Integer, db.ForeignKey('especialistas.especialista_id'), nullable=False)
    fecha_inicio = db.Column(db.TIMESTAMP(timezone=True), nullable=False)
    fecha_fin = db.Column(db.TIMESTAMP(timezone=True), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)

    def __init__(self, cita_id, usuario_id, especialista_id, descripcion, fecha_inicio, fecha_fin):
        self.usuario_id = usuario_id
        self.especialista_id = especialista_id
        self.cita_id = cita_id
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin