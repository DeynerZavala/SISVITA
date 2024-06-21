from datetime import datetime
from flask import Blueprint, request, make_response, jsonify

from models.especialistas import Especialistas
from models.usuarios import Usuarios
from schemas.especialistas_schema import especialista_schema
from schemas.usuarios_schema import usuarios_schema, usuario_schema
from utils.db import db
from werkzeug.security import generate_password_hash, check_password_hash

usuarios_routes = Blueprint('usuarios_routes', __name__)

@usuarios_routes.route('/usuarios', methods=['POST'])
def create_usuario():
    nombre = request.json.get('nombre')
    apellido_paterno = request.json.get('apellido_paterno')
    apellido_materno = request.json.get('apellido_materno')
    correo_electronico = request.json.get('correo_electronico')
    contrasena = request.json.get('contrasena')
    ubigeo = request.json.get('ubigeo')

    # Validar que los datos requeridos estén presentes
    if not all([nombre, apellido_paterno, correo_electronico, contrasena,ubigeo]):
        return make_response(jsonify({'message': 'Datos incompletos', 'status': 400}), 200)

    existing_usuario = Usuarios.query.filter_by(correo_electronico=correo_electronico).first()
    if existing_usuario:
        return make_response(jsonify({'message': 'Correo electrónico ya registrado', 'status': 400}), 200)

    existing_especialista= Especialistas.query.filter_by(correo_electronico=correo_electronico).first()
    if existing_especialista:
        return make_response(jsonify({'message': 'Correo electrónico ya registrado', 'status': 400}), 200)
    # Hash de la contraseña usando pbkdf2:sha256
    hashed_contrasena = generate_password_hash(contrasena, method='pbkdf2:sha256')

    # Crear una nueva instancia del modelo Usuarios
    new_usuario = Usuarios(
        nombre=nombre,
        apellido_paterno=apellido_paterno,
        apellido_materno=apellido_materno,
        correo_electronico=correo_electronico,
        contrasena=hashed_contrasena,
        fecha_registro=datetime.now(),
        ubigeo=ubigeo# Usar la fecha y hora actual con zona horaria
    )

    try:
        db.session.add(new_usuario)
        db.session.commit()
        result = usuario_schema.dump(new_usuario)
        data = {
            'message': 'Nuevo Usuario creado',
            'status': 201,
            'data': result
        }
        return make_response(jsonify(data), 200)
    except Exception as e:
        db.session.rollback()
        return make_response(jsonify({'message': 'Error al crear el usuario', 'status': 500}), 200)

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
        return make_response(jsonify(data), 200)

    result = usuario_schema.dump(usuario)

    data = {
        'message': 'El usuario encontrado',
        'status': 200,
        'data': result
    }
    return make_response(jsonify(data), 200)


@usuarios_routes.route('/usuarios/<int:id>', methods=['PUT'])
def update_usuario(id):
    usuario = Usuarios.query.get(id)
    if not usuario:
        data = {
            'message': 'El usuario no encontrado',
            'status': 404,
        }
        return make_response(jsonify(data), 200)
    nombre = request.json.get('nombre')
    apellido_paterno = request.json.get('apellido_paterno')
    apellido_materno = request.json.get('apellido_materno')
    correo_electronico = request.json.get('correo_electronico')
    contrasena = request.json.get('contrasena')

    usuario.nombre = nombre
    usuario.apellido_paterno = apellido_paterno
    usuario.apellido_materno = apellido_materno
    usuario.correo_electronico = correo_electronico

    if contrasena:
        usuario.contrasena = generate_password_hash(contrasena, method='pbkdf2:sha256')

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
        return make_response(jsonify(data), 200)

    db.session.delete(usuario)
    db.session.commit()
    data = {
        'message': 'El usuario eliminado',
        'status': 200,
    }
    return make_response(jsonify(data), 200)


@usuarios_routes.route('/usuarios/login', methods=['POST'])
def login():
    data = request.json

    if not data or 'correo_electronico' not in data or 'contrasena' not in data:
        return make_response(jsonify({'message': 'Credenciales incompletas', 'status': 400}), 200)

    correo_electronico = data['correo_electronico']
    contrasena = data['contrasena']

    usuario = Usuarios.query.filter_by(correo_electronico=correo_electronico).first()
    if usuario and check_password_hash(usuario.contrasena, contrasena):
        result = usuario_schema.dump(usuario)
        return make_response(jsonify({'message': 'Inicio de sesión exitoso', 'status': 200, 'data': result, 'rol': "Usuario"}), 200)

    especialista = Especialistas.query.filter_by(correo_electronico=correo_electronico).first()
    if especialista and check_password_hash(especialista.contrasena, contrasena):
        result = especialista_schema.dump(especialista)
        return make_response(jsonify({'message': 'Inicio de sesión exitoso', 'status': 200, 'data': result, 'rol': "Especialista"}), 200)

    return make_response(jsonify({'message': 'Credenciales inválidas', 'status': 400}), 200)
