
from flask import Blueprint, make_response, jsonify, request

from models.tratamientos import Tratamientos
from schemas.tratamientos_schema import  tratamientos_schema


tratamientos_routes = Blueprint('tratamientos_routes', __name__)

@tratamientos_routes.route('/tratamientos', methods=['GET'])
def get_tratamientos():
    all_tratamientos = Tratamientos.query.all()
    result = tratamientos_schema.dump(all_tratamientos)
    print(result)
    data = {
        'message': 'Todo los Tratamientos',
        'status': 200,
        'data': result
    }
    return make_response(jsonify(data), 200)
