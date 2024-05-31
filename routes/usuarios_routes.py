import datetime
from flask import Blueprint, request, make_response, jsonify
from models.usuarios import Usuarios
from schemas.usuarios_schema import usuarios_schema, usuario_schema
from utils.db import db

usuarios_routes = Blueprint('usuarios_routes', __name__)


@usuarios_routes.route('/usuarios', methods=['POST'])
def create_usuario():
    usuario = request.json.get('usuario')
    apellido_paterno = request.json.get('apellido_paterno')
    apellido_materno = request.json.get('apellido_materno')
    correo_electronico = request.json.get('correo_electronico')
    fecha_registro = datetime.date.today()
    contrasena = request.json.get('contrasena')

    new_usuario = Usuarios(usuario, apellido_paterno, apellido_materno,
                           correo_electronico,  contrasena, fecha_registro)

    db.session.add(new_usuario)
    db.session.commit()
    result = usuario_schema.dump(new_usuario)
    data={
        'message':'Nuevo Usuario creado',
        'status': 201,
        'data': result
    }
    return make_response(jsonify(data), 201)
@usuarios_routes.route('/usuarios', methods=['GET'])
def get_usuarios():
    all_usuarios = Usuarios.query.all()
    result = usuarios_schema.dump(all_usuarios)
    data = {
        'message': 'Todo el Personal',
        'status': 200,
        'data': result
    }
    return make_response(jsonify(data), 200)


@usuarios_routes.route('/usuarios/<int:id>', methods=['GET'])
def get_usuario(id):
    usuario = Usuarios.query.get(id)
    if not usuario:
        data = {
            'message': 'El usuario no encontrado',
            'status': 404,
        }
        return make_response(jsonify(data), 404)

    result = usuario_schema.dump(usuario)

    data = {
        'message': 'El usuario eencontrado',
        'status': 200,
        'data': result
    }
    return  make_response(jsonify(data), 200)

@usuarios_routes.route('/usuarios/<int:id>', methods=['PUT'])
def update_usuario(id):
    usuario = Usuarios.query.get(id)
    if not usuario:
        data = {
            'message': 'El usuario no encontrado',
            'status': 404,
        }
        return make_response(jsonify(data), 404)
    nombre = request.json.get('nombre')
    apellido_paterno = request.json.get('apellido_paterno')
    apellido_materno = request.json.get('apellido_materno')
    correo_electronico = request.json.get('correo_electronico')
    contrasena = request.json.get('contrasena')

    usuario.nombre = nombre
    usuario.apellido_paterno = apellido_paterno
    usuario.apellido_materno = apellido_materno
    usuario.contrasena = contrasena
    usuario.correo_electronico = correo_electronico

    db.session.commit()

    result = usuario_schema.dump(usuario)

    data = {
        'message': 'El usuario actualizado',
        'status': 200,
        'data': result
    }
    return make_response(jsonify(data), 200)


@usuarios_routes.route('/usuarios/<int:id>', methods=['DELETE'])
def delete_usuario(id):
    usuario = Usuarios.query.get(id)
    if not usuario:
        data = {
            'message': 'El usuario no encontrado',
            'status': 404,
        }
        return make_response(jsonify(data), 404)

    db.session.delete(usuario)
    db.session.commit()
    data = {
        'message': 'El usuario eliminado',
        'status': 200,
    }
    return make_response(jsonify(data), 200)
