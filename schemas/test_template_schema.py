from utils.ma import ma
from models.test_template import Test_Templates

class Test_TemplatesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Test_Templates
        fields = ('template_id','min',
                  'max','test_id','ans_sem_id')
test_template_schema = Test_TemplatesSchema()
test_templates_schema = Test_TemplatesSchema(many=True)