from utils.ma import ma
from models.tratamientos import Tratamientos

class TratamientosSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Tratamientos
        fields = ('tratamiento_id','tratamiento_nombre')
tratamiento_schema = TratamientosSchema()
tratamientos_schema = TratamientosSchema(many=True)