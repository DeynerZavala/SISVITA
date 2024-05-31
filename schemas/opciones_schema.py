from models.opciones import Opciones
from utils.ma import ma
class OpcionesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Opciones
        fields = ('opciones_id','pregunta_id','textoopcion','escorrecta')

opcion_schema = OpcionesSchema()
opciones_schema = OpcionesSchema(many=True)