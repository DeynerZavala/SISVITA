from flask import Blueprint, make_response, jsonify

from models.opciones import Opciones
from models.preguntas import Preguntas
from models.tests import Tests
from schemas.tests_schema import tests_schema, test_schema
from utils.db import db

test_routes = Blueprint('test_routes', __name__)


@test_routes.route('/test', methods=['GET'])
def get_tests():
    all_usuario = Tests.query.all()
    result = tests_schema.dump(all_usuario)
    data = {
        'message': 'Todo los test',
        'status': 200,
        'data': result
    }
    return make_response(jsonify(data), 200)


@test_routes.route('/test/<int:id>', methods=['GET'])
def get_test(id):
    test = Tests.query.get(id)
    if test is None:
        data = {
            'message': 'No existe el test',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    result = test_schema.dump(test)

    data = {
        'message': 'Test encontrado',
        'status': 200,
        'data': result
    }
    return make_response(jsonify(data), 200)
@test_routes.route('/test/all', methods=['GET'])
def get_all_tests():
    response = []
    data = (
        db.session.query(
            Tests.test_id.label('test_id'),
            Tests.descripcion.label('test_description'),
            Tests.fecha_creacion.label('fecha_creacion'),
            Preguntas.pregunta_id.label('pregunta_id'),
            Preguntas.textopregunta.label('textopregunta'),
        )
        .join(Tests, Preguntas.test_id == Tests.test_id)
        .all()
    )

    for row in data :
        response.append({
            "test_id": row[0],
            "test_description": row[1],
            "fecha_creacion": row[2],
            "pregunta_id": row[3],
            "textopregunta": row[4],
        })
    if response:
        return jsonify(response)
    else:
        return jsonify({'message': 'No se encontraron datos', 'status': 404})

@test_routes.route('/test/all/<int:id>', methods=['GET'])
def get_all_test(id):
    test = Tests.query.get(id)
    if test is None:
        return jsonify({'message': 'No existe el test', 'status': 404})
    preguntas = test.preguntas
    preguntas_data =[
        {
            'pregunta_id': pregunta.pregunta_id,
            'textopregunta': pregunta.textopregunta,
        }
        for pregunta in preguntas
    ]
    return make_response(jsonify(preguntas_data), 200)