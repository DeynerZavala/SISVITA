from utils.ma import ma
from models.ansiedad import Ansiedad


class Ansiedad_SemaforoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Ansiedad
        fields = ('ans_sem_id', 'semaforo')


ansiedad_semaforo_schema = Ansiedad_SemaforoSchema()
ansiedades_semaforo_schema = Ansiedad_SemaforoSchema(many=True)