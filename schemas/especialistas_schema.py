from models.especialistas import Especialistas
from utils.ma import ma


class EspecialistasSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Especialistas
        fields = ('especialista_id','nombre','apellido_paterno',
                  'apellido_materno','correo_electronico',
                  'contrasena','fecha_registro','titulo')
especialista_schema = EspecialistasSchema()
especialistas_schema = EspecialistasSchema(many=True)