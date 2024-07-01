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