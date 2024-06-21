from datetime import datetime
from flask import Blueprint, request, make_response, jsonify

from models.titulo import Titulos
from schemas.titulo_schema import titulos_schema

from utils.db import db

titulo_routes = Blueprint('titulo_routes', __name__)

@titulo_routes.route('/titulo', methods=['GET'])
def get_titulo():
    all_titulo = Titulos.query.all()
    result = titulos_schema.dump(all_titulo)
    data = {
        'message': "Todo los titulo",
        'status': 200,
        'data': result
    }
    return make_response(jsonify(data), 200)
