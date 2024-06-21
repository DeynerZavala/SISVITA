import sqlalchemy
from flask import Blueprint, make_response, jsonify, request

from models.opciones import Opciones
from models.opciones_predeterminadas import Opciones_predeterminadas
from models.preguntas import Preguntas
from models.respuesta import Respuestas
from models.respuesta_usuario import Respuesta_Usuario
from models.template import Templates
from models.tests import Tests
from schemas.respuesta_schema import respuesta_schema
from schemas.respuesta_usuario_schema import respuesta_usuario_schema
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
        return make_response(jsonify(data), 200)
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
            Tests.titulo.label('titulo'),
            Tests.descripcion.label('test_description'),
            Tests.fecha_creacion.label('fecha_creacion'),
            Preguntas.pregunta_id.label('pregunta_id'),
            Preguntas.textopregunta.label('textopregunta'),
            Opciones.opcion_id.label('opcion_id'),
            Opciones.op_pre_id.label('op_pre_id'),
            Opciones_predeterminadas.nombre.label('nombre')
        )
        .join(Preguntas, Preguntas.test_id == Tests.test_id)
        .outerjoin(Opciones, Opciones.pregunta_id == Preguntas.pregunta_id)
        .join(Opciones_predeterminadas, Opciones_predeterminadas.op_pre_id == Opciones.op_pre_id)
        .all()
    )

    temp_response = {}

    for row in data:
        test_id = row.test_id
        pregunta_id = row.pregunta_id

        if test_id not in temp_response:
            temp_response[test_id] = {
                "test_id": test_id,
                "titulo": row.titulo,
                "test_description": row.test_description,
                "fecha_creacion": row.fecha_creacion,
                "preguntas": {}
            }

        if pregunta_id not in temp_response[test_id]["preguntas"]:
            temp_response[test_id]["preguntas"][pregunta_id] = {
                "pregunta_id": pregunta_id,
                "textopregunta": row.textopregunta,
                "opciones": []
            }

        if row.opcion_id:
            temp_response[test_id]["preguntas"][pregunta_id]["opciones"].append({
                "opcion_id": row.opcion_id,
                "op_pre_id": row.op_pre_id,
                "nombre": row.nombre
            })

    for test in temp_response.values():
        test['preguntas'] = list(test['preguntas'].values())
        response.append(test)

    if response:
        return make_response(jsonify({
            'message': 'Todos los test completos',
            'status': 200,
            'data': response}), 200)
    else:
        return make_response(jsonify({'message': 'No se encontraron datos', 'status': 404}), 200)


@test_routes.route('/test/all/<int:id>', methods=['GET'])
def get_all_test(id):
    response = []

    data = (
        db.session.query(
            Tests.test_id.label('test_id'),
            Tests.titulo.label('titulo'),
            Tests.descripcion.label('test_description'),
            Tests.fecha_creacion.label('fecha_creacion'),
            Preguntas.pregunta_id.label('pregunta_id'),
            Preguntas.textopregunta.label('textopregunta'),
            Opciones.opcion_id.label('opcion_id'),
            Opciones.op_pre_id.label('op_pre_id'),
            Opciones_predeterminadas.nombre.label('nombre')
        )
        .where(Tests.test_id == id)
        .join(Preguntas, Preguntas.test_id == Tests.test_id)
        .outerjoin(Opciones, Opciones.pregunta_id == Preguntas.pregunta_id)
        .join(Opciones_predeterminadas, Opciones_predeterminadas.op_pre_id == Opciones.op_pre_id)
        .all()
    )

    temp_response = {}

    for row in data:
        test_id = row.test_id
        pregunta_id = row.pregunta_id

        if test_id not in temp_response:
            temp_response[test_id] = {
                "test_id": test_id,
                "titulo": row.titulo,
                "test_description": row.test_description,
                "fecha_creacion": row.fecha_creacion,
                "preguntas": {}
            }

        if pregunta_id not in temp_response[test_id]["preguntas"]:
            temp_response[test_id]["preguntas"][pregunta_id] = {
                "pregunta_id": pregunta_id,
                "textopregunta": row.textopregunta,
                "opciones": []
            }

        if row.opcion_id:
            temp_response[test_id]["preguntas"][pregunta_id]["opciones"].append({
                "opcion_id": row.opcion_id,
                "op_pre_id": row.op_pre_id,
                "nombre": row.nombre
            })

    for test in temp_response.values():
        test['preguntas'] = list(test['preguntas'].values())
        response.append(test)

    if response:
        return make_response(jsonify({
            'message': 'Todos los test completos',
            'status': 200,
            'data': response}), 200)
    else:
        return make_response(jsonify({'message': 'No se encontraron datos', 'status': 404}), 200)






@test_routes.route('/test/responder', methods=['POST'])
def responder():
    try:
        fecha_fin = request.json.get('fecha_fin')
        preguntas = request.json.get('preguntas')
        usuario_id = request.json.get('usuario_id')
        if not all([fecha_fin, preguntas, usuario_id]):
            return make_response(jsonify({'message': 'Datos incompletos', 'status': 400}), 200)
        if any('pregunta_id' not in pregunta or 'opcion_id' not in pregunta for pregunta in preguntas):
            return make_response(jsonify({'message': 'Faltan datos en las preguntas', 'status': 400}), 200)

        new_respuesta_usuario = Respuesta_Usuario(usuario_id=usuario_id, fecha_fin=fecha_fin, puntuacion=0)
        db.session.add(new_respuesta_usuario)
        #db.session.commit()
        puntaje = 0

        for pregunta in preguntas:
            opcion_id = pregunta['opcion_id']
            opcion = Opciones.query.filter_by(opcion_id=opcion_id).first()
            puntaje+= opcion.valor

            new_respuesta = Respuestas(opcion_id=opcion_id,res_user_id=new_respuesta_usuario.res_user_id)
            db.session.add(new_respuesta)
            #db.session.commit()

        new_respuesta_usuario.puntuacion = puntaje
        db.session.add(new_respuesta_usuario)

        templates = (db.session.query(
            Templates.template_id.label('template_id'),
            Templates.estado.label('estado'),
            Templates.max.label('max'),
            Templates.min.label('min'),
        )
            .where(Preguntas.pregunta_id == pregunta['pregunta_id'])
            .where(Preguntas.test_id == Tests.test_id)
            .where(Tests.test_id == Templates.test_id)
            .all()
        )
        for row in templates:
            min = row.min
            max = row.max
            if (puntaje <= max and puntaje >= min):
                semaforo = row.estado
                break
        data = {
            'message': 'Respuesta Guardada',
            'puntuacion': puntaje,
            'semaforo' : semaforo,
            'status': 200,
        }
        db.session.commit()

        return make_response(jsonify(data), 200)
    except Exception as e:
        db.session.rollback()
        print(e)
        return make_response(jsonify({'message': 'Error al guardar respuesta', 'status': 500}), 200)
