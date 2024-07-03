import sqlalchemy
from flask import Blueprint, make_response, jsonify, request
from sqlalchemy import func
from sqlalchemy.sql.operators import and_

from models.ansiedad import Ansiedad
from models.ansiedad_semaforo import Ansiedad_Semaforo
from models.diagnostico import Diagnostico
from models.opciones import Opciones
from models.opciones_predeterminadas import Opciones_predeterminadas
from models.preguntas import Preguntas
from models.respuesta import Respuestas
from models.respuesta_usuario import Respuesta_Usuario
from models.test_template import Test_Templates
from models.tests import Tests
from models.ubigeo import Ubigeo
from models.usuarios import Usuarios
from schemas.ansiedad_semaforo_schema import ansiedad_semaforo_schema
from schemas.diagnostico_schema import diagnostico_schema
from schemas.respuesta_schema import respuesta_schema
from schemas.respuesta_usuario_schema import respuesta_usuario_schema, respuestas_usuario_schema
from schemas.test_template_schema import test_template_schema, test_templates_schema, Test_TemplatesSchema
from schemas.tests_schema import tests_schema, test_schema
from schemas.usuarios_schema import usuarios_schema
from utils.db import db

diagnostico_routes = Blueprint('diagnostico_routes', __name__)


@diagnostico_routes.route('/diagnostico', methods=['GET'])
def get_diagnostico():
    all_diagnostico = Diagnostico.query.all()
    result = diagnostico_schema.dump(all_diagnostico)
    print(result)
    data = {
        'message': 'Todo los diagnosticos',
        'status': 200,
        'data': result
    }
    return make_response(jsonify(data), 200)


@diagnostico_routes.route('/diagnostico', methods=['POST'])
def create_diagnostico():
    try:
        usuario_id = request.json['usuario_id']
        especialista_id = request.json['especialista_id']
        ansiedad_id = request.json['ansiedad_id']
        fecha = func.now()
        comunicacion_estudiante = request.json['comunicacion_estudiante']
        solicitar_cita = request.json['solicitar_cita']
        tratamiento_id = request.json['tratamiento_id']
        fundamentacion_cientifica = request.json['fundamentacion_cientifica']

        if not all([especialista_id,ansiedad_id, tratamiento_id,fundamentacion_cientifica,usuario_id]):
            return make_response(jsonify({'message': 'Datos incompletos', 'status': 400}), 200)
        if (comunicacion_estudiante== None and solicitar_cita==None):
            return make_response(jsonify({'message': 'Datos incompletos', 'status': 400}), 200)


        new_diagnostico = Diagnostico(especialista_id=especialista_id,ansiedad_id=ansiedad_id,fecha=fecha,comunicacion_estudiante=comunicacion_estudiante,
                                      solicitar_cita=solicitar_cita,tratamiento_id=tratamiento_id,fundamentacion_cientifica=fundamentacion_cientifica)
        db.session.add(new_diagnostico)
        db.session.commit()
        result = diagnostico_schema.dump(new_diagnostico)
        data = {
            'message': 'Nuevo Diagnostico creado',
            'status': 200,
            'data': result
        }
        return make_response(jsonify(data), 200)


    except Exception as e:
        db.session.rollback()
        print(e)
        return make_response(jsonify({'message': 'Error', 'status': 200}), 200)
