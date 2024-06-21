from models.respuesta_usuario import Respuesta_Usuario
from utils.ma import ma

class Respuesta_UsuarioSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Respuesta_Usuario
        fields = ('res_user_id', 'usuario_id', 'diagnostico_id','fecha_fin', 'puntuacion')
respuesta_usuario_schema = Respuesta_UsuarioSchema()
respuestas_usuario_schema =Respuesta_UsuarioSchema(many=True)