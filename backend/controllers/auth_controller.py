from flask import Blueprint, request, jsonify
from sqlalchemy import try_cast
from werkzeug.security import generate_password_hash
from models import db, User
from services.auth_service import AuthService

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    try:
        validator = AuthService.validar_usuario(data.get('email'),data.get('clave'))
        if not validator:
            return jsonify({'message': False}), 200
        else:
            return jsonify({'message': True}), 200
    except Exception as e:
        return jsonify({'error': 'Ocurrió un error al autenticar.'}), 500


@auth_bp.route('/users', methods=['GET'])
def get_all_users():
    users_list = []
    try:
        users_list = AuthService.obtener_usuarios()
        if not users_list.count():
            return jsonify({'message': 'No se encontraron usuarios.'}),404
    except Exception as e:
        # Captura cualquier error inesperado y devuelve un error 500.
        print("Error al buscar usuarios. " + e)
        return jsonify({'error': 'Ocurrió un error inesperado al obtener los usuarios.'}), 500
    finally:
        return jsonify(users_list), 200
