from datetime import datetime

from flask import Blueprint, request

respuesta_routes = Blueprint('respuesta_routes', __name__)
@respuesta_routes.route('/respuesta', methods=['POST'])
def create_respuesta():
    usuario_id = request.json.get('usuario_id')
    respuesta_id = request.json.get('respuesta_id')
    fecha_fin = datetime.date.today()


