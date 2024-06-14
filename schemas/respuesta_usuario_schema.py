from models.respuesta_usuario import Respuesta_Usuario
from utils.ma import ma

class Respuesta_UsuarioSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Respuesta_Usuario
        fields = ('respuesta_id','pregunta_id','opcion_id','es_correcto')
respuesta_usuario_schema = Respuesta_UsuarioSchema()
respuestas_usuario_schema =Respuesta_UsuarioSchema(many=True)