from models.opciones import Opciones
from utils.ma import ma
class OpcionesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Opciones
        fields = ('opcion_id','pregunta_id','op_pre_id','valor')

opcion_schema = OpcionesSchema()
opciones_schema = OpcionesSchema(many=True)