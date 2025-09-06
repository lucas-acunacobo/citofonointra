from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from services.auth_service import AuthService

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['POST'])
@cross_origin()
def login():
    data = request.get_json()
    try:
        user = AuthService.validar_usuario(data.get('email'),data.get('clave'))
        if not user:
            print("Usuario ",data.get('email')," no Autorizado")
            return jsonify({'message': False}), 200
        else:
            print("Usuario ",data.get('email')," Autorizado")
            print(user)
            return (jsonify({'id':user.id,
                            'nombre':user.nombre,
                            'apellidopaterno':user.apellido_paterno,
                            'apellidomaterno':user.apellido_materno,
                            'email':user.email}),
                    200)
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
