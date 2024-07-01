from utils.db import db

class Ubigeo(db.Model):
    __tablename__ = 'ubigeo'

    ubigeo_id = db.Column(db.Integer, primary_key=True)
    departamento = db.Column(db.String(255))
    provincia = db.Column(db.String(255))
    distrito = db.Column(db.String(255))
    latitud = db.Column(db.Numeric(asdecimal=True))  # Double Precision
    longitud = db.Column(db.Numeric(asdecimal=True))  # Double Precision

    def __init__(self, ubigeo_id, departamento, provincia, distrito, latitud, longitud):
        self.ubigeo_id = ubigeo_id
        self.departamento = departamento
        self.provincia = provincia
        self.distrito = distrito
        self.latitud = latitud
        self.longitud = longitud
