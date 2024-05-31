from flask import Blueprint, make_response, jsonify

from models.preguntas import Preguntas
from schemas.preguntas_schema import preguntas_schema
from schemas.tests_schema import tests_schema, test_schema

preguntas_routes = Blueprint('preguntas_routes', __name__)


@preguntas_routes.route('/preguntas', methods=['GET'])
def get_preguntas():
    all_preguntas = Preguntas.query.all()
    result = preguntas_schema.dump(all_preguntas)
    data = {
        'message': 'Todas las preguntas',
        'status': 200,
        'data': result
    }
    return make_response(jsonify(data), 200)


@preguntas_routes.route('/preguntas/<int:id>', methods=['GET'])
def get_tests(id):
    test = Preguntas.query.get(id)
    if test is None:
        data = {
            'message': 'No se encuentra la pregunta',
            'status': 404,
        }
        return make_response(jsonify(data), 404)
    result = test_schema.dump(test)

    data = {
        'message': 'Pregunta encontrado',
        'status': 200,
        'data': result
    }
    return make_response(jsonify(data), 200)
