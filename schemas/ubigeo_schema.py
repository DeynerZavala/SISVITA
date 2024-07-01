from utils.ma import ma
from models.ubigeo import Ubigeo

class UbigeoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Ubigeo
        fields = ('ubigeo_id', 'departamento', 'provincia', 'distrito', 'latitud', 'longitud')

ubigeo_schema = UbigeoSchema()
ubigeos_schema = UbigeoSchema(many=True)
