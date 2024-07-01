from datetime import datetime
from flask import Blueprint, request, make_response, jsonify

from models.ansiedad_semaforo import Ansiedad_Semaforo
from models.especialistas import Especialistas
from models.usuarios import Usuarios
from schemas.ansiedad_semaforo_schema import ansiedad_semaforo_schema, ansiedades_semaforo_schema
from schemas.especialistas_schema import especialistas_schema, especialista_schema
from werkzeug.security import generate_password_hash, check_password_hash
from utils.db import db

ansiedad_semaforo_routes = Blueprint('ansiedad_semaforo_routes', __name__)

@ansiedad_semaforo_routes.route('/ansiedad-semaforo', methods=['GET'])
def getAnsiedadSemaforo():
    AnsiedadSemaforo = Ansiedad_Semaforo.query.all()
    result = ansiedades_semaforo_schema.dump(AnsiedadSemaforo)
    data = {
        'message': "Todo Ansiedad Semaforo",
        'status': 200,
        'data': result
    }
    return make_response(jsonify(data), 200)


