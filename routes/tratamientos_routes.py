import sqlalchemy
from flask import Blueprint, make_response, jsonify, request
from sqlalchemy import func
from sqlalchemy.sql.operators import and_

from models import tratamientos
from models.ansiedad import Ansiedad
from models.ansiedad_semaforo import Ansiedad_Semaforo
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
from schemas.tratamientos_schema import tratamientos_schema, tratamiento_schema
from schemas.respuesta_schema import respuesta_schema
from schemas.respuesta_usuario_schema import respuesta_usuario_schema, respuestas_usuario_schema
from schemas.test_template_schema import test_template_schema, test_templates_schema, Test_TemplatesSchema
from schemas.tests_schema import tests_schema, test_schema
from schemas.usuarios_schema import usuarios_schema
from utils.db import db

tratamientos_routes = Blueprint('tratamientos_routes', __name__)

@tratamientos_routes.route('/tratamientos', methods=['GET'])
def get_tratamientos():
    all_tratamientos = tratamientos.query.all()
    result = tratamiento_schema.dump(all_tratamientos)
    print(result)
    data = {
        'message': 'Todo los Tratamientos',
        'status': 200,
        'data': result
    }
    return make_response(jsonify(data), 200)
