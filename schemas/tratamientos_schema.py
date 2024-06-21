from utils.ma import ma
from models.tratamientos import Tratamientos

class TratamientosSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Tratamientos
        fields = ('tratamiento_id', 'usuario_id', 'especialista_id','tratamiento_nombre','descripcion',
                  'fecha_inicio', 'fecha_fin')
tratamiento_schema = TratamientosSchema()
tratamientos_schema = TratamientosSchema(many=True)