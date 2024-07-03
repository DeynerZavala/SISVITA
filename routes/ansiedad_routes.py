from datetime import datetime
from flask import Blueprint, request, make_response, jsonify

from models.ansiedad import Ansiedad
from models.ansiedad_semaforo import Ansiedad_Semaforo
from models.especialistas import Especialistas
from models.usuarios import Usuarios
from schemas.ansiedad_schema import ansiedades_schema
from schemas.ansiedad_semaforo_schema import ansiedad_semaforo_schema, ansiedades_semaforo_schema
from schemas.especialistas_schema import especialistas_schema, especialista_schema
from werkzeug.security import generate_password_hash, check_password_hash
from utils.db import db

ansiedad_routes = Blueprint('ansiedad_routes', __name__)

@ansiedad_routes.route('/ansiedad', methods=['GET'])
def getAnsiedadSemaforo():
    AnsiedadSemaforo = Ansiedad.query.all()
    result = ansiedades_schema.dump(AnsiedadSemaforo)
    data = {
        'message': "Todo Ansiedad ",
        'status': 200,
        'data': result
    }
    return make_response(jsonify(data), 200)


