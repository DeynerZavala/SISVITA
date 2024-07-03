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


