from utils.db import db
from models.foros import Foros
from models.usuarios import Usuarios




class MensajesForos(db.Model):
    __tablename__ = 'Mensajes_Foros'
    
    mensaje_id = db.Column(db.Integer, primary_key=True)
    foro_id = db.Column(db.Integer, db.ForeignKey('Foros.foro_id'), nullable=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('Usuarios.usuario_id'), nullable=True)
    contenido = db.Column(db.Text, nullable=True)
    fecha_publicacion = db.Column(db.Date, nullable=True)

    def __init__(self, mensaje_id, foro_id, usuario_id, contenido, fecha_publicacion):
        self.mensaje_id = mensaje_id
        self.foro_id = foro_id
        self.usuario_id = usuario_id
        self.contenido = contenido
        self.fecha_publicacion = fecha_publicacion