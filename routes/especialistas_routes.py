from datetime import datetime
from flask import Blueprint, request, make_response, jsonify
from models.especialistas import Especialistas
from schemas.especialistas_schema import especialistas_schema
from utils.db import db

especialistas_routes = Blueprint('especialistas_routes', __name__)


@especialistas_routes.route('/especialistas', methods=['POST'])
def create_especialista():
    nombres = request.json.get('nombres')
    apellido_paterno = request.json.get('apellido_paterno')
    apellido_materno = request.json.get('apellido_materno')
    correo_electronico = request.json.get('correo_electronico')
    contrasena = request.json.get('contrasena')
    titulo = request.json.get('titulo')
    fecha_registro = datetime.date.today()

    new_especialista = Especialistas(nombres, apellido_paterno, apellido_materno, titulo,
                                     correo_electronico, contrasena, fecha_registro)
    db.session.add(new_especialista)
    db.session.commit()

    result = especialistas_schema.dump(new_especialista)
    data = {
        'message': 'Nuevo especialista creado.',
        'status': 201,
        'data': result
    }
    return make_response(jsonify(data), 201)


@especialistas_routes.route('/especialistas', methods=['GET'])
def get_especialistas():
    all_especialistas = Especialistas.query.all()
    result = especialistas_schema.dump(all_especialistas)
    data = {
        'message': "Todo los Especialistas",
        'status': 200,
        'data': result
    }
    return make_response(jsonify(data), 200)


@especialistas_routes.route('/especialistas/<int:id>', methods=['GET'])
def get_especialista(id):
    especialista = Especialistas.query.get(id)
    if not especialista:
        data = {
            'message': "Especialista no encontrado",
            'status': 404,
        }
        return make_response(jsonify(data), 404)
    result = especialistas_schema.dump(especialista)
    data = {
        'message': "Especialista encontrado",
        'status': 200,
        'data': result
    }
    return make_response(jsonify(data), 200)


@especialistas_routes.route('/especialistas/<int:id>', methods=['PUT'])
def update_especialista(id):
    especialista = Especialistas.query.get(id)
    if not especialista:
        data = {
            'message': "Especialista no encontrado",
            'status': 404,
        }
        return make_response(jsonify(data), 404)
    nombres = request.json.get('nombres')
    apellido_paterno = request.json.get('apellido_paterno')
    apellido_materno = request.json.get('apellido_materno')
    correo_electronico = request.json.get('correo_electronico')
    fecha_registro = request.json.get('fecha_registro')
    contrasena = request.json.get('contrasena')
    titulo = request.json.get('titulo')

    especialista.nombres = nombres
    especialista.apellido_paterno = apellido_paterno
    especialista.apellido_materno = apellido_materno
    especialista.fecha_registro = fecha_registro
    especialista.contrasena = contrasena
    especialista.titulo = titulo
    especialista.correo_electronico = correo_electronico

    db.session.commit()

    result = especialistas_schema.dump(especialista)

    data = {
        'message': "Especialista actualizado",
        'status': 200,
        'data': result
    }
    return make_response(jsonify(data), 200)


@especialistas_routes.route('/especialistas/<int:id>', methods=['DELETE'])
def delete_especialista(id):
    especialista = Especialistas.query.get(id)
    if not especialista:
        data = {
            'message': "Especialista no encontrado",
            'status': 404,
        }
        return make_response(jsonify(data), 404)
    db.session.delete(especialista)
    db.session.commit()

    data = {
        'message': "Especialista eliminado",
        'status': 200,
    }
    return make_response(jsonify(data), 200)
