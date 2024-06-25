from datetime import datetime
from flask import Blueprint, request, make_response, jsonify
from models.especialistas import Especialistas
from models.usuarios import Usuarios
from schemas.especialistas_schema import especialistas_schema, especialista_schema
from werkzeug.security import generate_password_hash, check_password_hash
from utils.db import db

especialistas_routes = Blueprint('especialistas_routes', __name__)


@especialistas_routes.route('/especialistas', methods=['POST'])
def create_especialista():
    nombre = request.json.get('nombre')
    apellido_paterno = request.json.get('apellido_paterno')
    apellido_materno = request.json.get('apellido_materno')
    correo_electronico = request.json.get('correo_electronico')
    contrasena = request.json.get('contrasena')
    titulo_id = request.json.get('titulo_id')
    ubigeo = request.json.get('ubigeo')

    # Validar que los datos requeridos estén presentes
    if not all([nombre, apellido_paterno, correo_electronico, contrasena, titulo_id, ubigeo]):
        return make_response(jsonify({'message': 'Datos incompletos', 'status': 400}), 200)

    existing_usuario = Usuarios.query.filter_by(correo_electronico=correo_electronico).first()
    if existing_usuario:
        return make_response(jsonify({'message': 'Correo electrónico ya registrado', 'status': 400}), 200)

    existing_especialista = Especialistas.query.filter_by(correo_electronico=correo_electronico).first()
    if existing_especialista:
        return make_response(jsonify({'message': 'Correo electrónico ya registrado', 'status': 400}), 200)

    # Hash de la contraseña usando pbkdf2:sha256
    hashed_contrasena = generate_password_hash(contrasena, method='pbkdf2:sha256')

    # Crear una nueva instancia del modelo Especialistas
    new_especialista = Especialistas(
        nombre=nombre,
        apellido_paterno=apellido_paterno,
        apellido_materno=apellido_materno,
        correo_electronico=correo_electronico,
        contrasena=hashed_contrasena,
        fecha_registro=datetime.now(),  # Usar la fecha y hora actual con zona horaria
        titulo_id=titulo_id,
        ubigeo=ubigeo
    )

    try:
        db.session.add(new_especialista)
        db.session.commit()
        result = especialista_schema.dump(new_especialista)
        data = {
            'message': 'Nuevo Especialista creado',
            'status': 201,
            'data': result
        }
        return make_response(jsonify(data), 200)
    except Exception as e:
        print(e)
        db.session.rollback()
        return make_response(jsonify({'message': 'Error al crear el especialista', 'status': 500}), 200)


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

