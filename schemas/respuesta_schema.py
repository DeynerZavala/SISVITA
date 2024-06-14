from utils.ma import ma
from models.usuarios import Usuarios

class RespuestasSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Usuarios
        fields = ('respuesta_id','pregunta_id','opcion_id','es_correcto')
respuesta_schema = RespuestasSchema()
respuestas_schema =RespuestasSchema(many=True)