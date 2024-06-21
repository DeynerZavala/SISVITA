from utils.ma import ma
from models.diagnostico import Diagnostico

class DiagnosticosSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Diagnostico
        fields = ('diagnostico_id','especialista_id', 'ansiedad_id','fecha',
                  'observaciones', 'solicitar_cita')
diagnostico_schema = DiagnosticosSchema()
diagnosticos_schema = DiagnosticosSchema(many=True)