from models.tests import Tests
from utils.ma import ma


class UsuariosSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Tests
        fields = ('test_id','descripcion','fecha_creacion')
test_schema = UsuariosSchema()
tests_schema = UsuariosSchema(many=True)