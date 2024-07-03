from utils.ma import ma
from models.diagnostico import Diagnostico

class DiagnosticosSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Diagnostico
        fields = ('diagnostico_id','diagnostico_id', 'ansiedad_id','fecha',
                  'comunicacion_estudiante', 'solicitar_cita','tratamiento_id','fundamentacion_cientifica')
diagnostico_schema = DiagnosticosSchema()
diagnosticos_schema = DiagnosticosSchema(many=True)