from models.titulo import Titulos
from utils.ma import ma


class TitulosSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Titulos
        fields = ('titulo_id','titulo_name')
titulo_schema = TitulosSchema()
titulos_schema = TitulosSchema(many=True)