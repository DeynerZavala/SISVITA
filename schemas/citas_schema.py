from utils.ma import ma
from models.citas import Citas

class CitasSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Citas
        fields = ('cita_id','usuario_id','especialista_id','fecha_inicio',
                  'fecha_fin', 'descripcion')
cita_schema = CitasSchema()
citas_schema = CitasSchema(many=True)