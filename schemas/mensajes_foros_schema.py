from models.mensajes_foros import MensajesForos
from utils.ma import ma


class MensajesForosSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = MensajesForos
        fields = ('mensaje_id','foro_id', 'usuario_id','contenido',
                  'fecha_publicacion')
mensaje_foros_schema = MensajesForosSchema()
mensajes_foros_schema = MensajesForosSchema(many=True)