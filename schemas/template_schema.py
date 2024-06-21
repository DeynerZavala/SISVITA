from utils.ma import ma
from models.template import Templates

class TemplatesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Templates
        fields = ('template_id','min',
                  'max','test_id')
template_schema = TemplatesSchema()
templates_schema = TemplatesSchema(many=True)