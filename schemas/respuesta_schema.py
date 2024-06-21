from utils.ma import ma
from models.respuesta import Respuestas

class RespuestasSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Respuestas
        fields = ('respuesta_id','opcion_id','res_user_id')
respuesta_schema = RespuestasSchema()
respuestas_schema =RespuestasSchema(many=True)