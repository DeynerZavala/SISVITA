from utils.ma import ma
from models.usuarios import Usuarios

class UsuariosSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Usuarios
        fields = ('usuario_id','nombre','apellido_paterno',
                  'apellido_materno','correo_electronico',
                  'contrasena','fecha_registro', 'ubigeo')
usuario_schema = UsuariosSchema()
usuarios_schema = UsuariosSchema(many=True)