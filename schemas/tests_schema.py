from models.tests import Tests
from utils.ma import ma


class TestSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Tests
        fields = ('test_id','titulo','descripcion','fecha_creacion', 'template_id')
test_schema = TestSchema()
tests_schema = TestSchema(many=True)