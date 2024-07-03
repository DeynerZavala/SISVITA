from utils.ma import ma
from models.ansiedad import Ansiedad

class AnsiedadSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Ansiedad
        fields = ('ansiedad_id','nivel','ans_sem_id')
        
ansiedad_schema = AnsiedadSchema()
ansiedades_schema = AnsiedadSchema(many=True)