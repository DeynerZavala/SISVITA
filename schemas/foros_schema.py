from models.foros import Foros
from utils.ma import ma


class ForosSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Foros
        fields = ('foro_id', 'especialista_id','tema','descripcion',
                  'fecha_creacion')
foro_schema = ForosSchema()
foros_schema = ForosSchema(many=True)