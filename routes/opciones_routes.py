from flask import Blueprint,make_response,jsonify

from models.opciones import Opciones
from schemas.opciones_schema import opciones_schema, opcion_schema

opciones_routes = Blueprint('opciones_routes', __name__)
@opciones_routes.route('/opciones', methods=['GET'])
def get_opciones():
    opciones = Opciones.query.all()
    result = opciones_schema.dump(opciones)
    data = {
        'message' : 'Todas las opciones',
        'status' : 200,
        'data' : result
    }
    return make_response(jsonify(data), 200)

@opciones_routes.route('/opciones/<int:id>', methods=['GET'])
def get_opcion(id):
    opcion = Opciones.query.get(id)
    if opcion is None:
        data ={
            'message' : 'No existe el opcion',
            'status' : 404,
        }
        return make_response(jsonify(data), 404)
    result = opcion_schema.dump(opcion)

    data = {
        'message' : 'Opcion encontrada',
        'status' : 200,
        'data' : result
    }
    return make_response(jsonify(data), 200)


