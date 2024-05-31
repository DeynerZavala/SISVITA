from models.preguntas import Preguntas
from utils.ma import ma
class PreguntasSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Preguntas
        fields = ('pregunta_id','test_id','textopregunta')

pregunta_schema = PreguntasSchema()
preguntas_schema = PreguntasSchema(many=True)