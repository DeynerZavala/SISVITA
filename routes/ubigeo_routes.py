from flask import Blueprint, request, make_response, jsonify
from models.ubigeo import Ubigeo
from schemas.ubigeo_schema import ubigeos_schema
from utils.db import db

ubigeo_routes = Blueprint('ubigeo_routes', __name__)

@ubigeo_routes.route('/ubigeo', methods=['GET'])
def get_ubigeos():
    ubigeos = Ubigeo.query.all()
    result = ubigeos_schema.dump(ubigeos)
    data = {
        'message': "Todos los Ubigeos",
        'status': 200,
        'data': result
    }
    return make_response(jsonify(data), 200)

#conseguir departamento, provincia, distrito  unicos
@ubigeo_routes.route('/departamentos', methods=['GET'])
def get_departamentos():
    departamentos = db.session.query(Ubigeo.departamento.distinct()).all()
    departamentos = [d[0] for d in departamentos]
    data = {
        'message': "Todos los Departamentos",
        'status': 200,
        'data': departamentos
    }
    return make_response(jsonify(data), 200)

@ubigeo_routes.route('/provincias/<departamento>', methods=['GET'])
def get_provincias(departamento):
    provincias = db.session.query(Ubigeo.provincia).filter_by(departamento=departamento).distinct().all()
    provincias = [p[0] for p in provincias]
    data = {
        'message': f"Provincias en {departamento}",
        'status': 200,
        'data': provincias
    }
    return make_response(jsonify(data), 200)

@ubigeo_routes.route('/distritos/<provincia>', methods=['GET'])
def get_distritos(provincia):
    distritos = db.session.query(Ubigeo.distrito).filter_by(provincia=provincia).distinct().all()
    distritos = [d[0] for d in distritos]
    data = {
        'message': f"Distritos en {provincia}",
        'status': 200,
        'data': distritos
    }
    return make_response(jsonify(data), 200)