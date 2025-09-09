from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from services.auth_service import AuthService

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/test', methods=['GET'])
@cross_origin()
def test():
    return jsonify({"data":"funciona!"}), 200

@auth_bp.route('/login', methods=['POST'])
@cross_origin()
def login():
    data = request.get_json()
    try:
        user = AuthService.validar_usuario(data.get('email'),data.get('clave'))
        if not user:
            print("Usuario ",data.get('email')," no Autorizado")
            return jsonify({}), 200
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
        print("Error al buscar usuarios. " + e)
        return jsonify({'error': 'Ocurrió un error inesperado al obtener los usuarios.'}), 500
    finally:
        return jsonify(users_list), 200

@auth_bp.route('/registrar', methods=['POST'])
@cross_origin()
def nuevo_registro():
    data = request.get_json()
    try:
        required_fields = ['nombre', 'apellido_paterno', 'apellido_materno', 'email', 'clave']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Faltan campos obligatorios.'}), 400
        respuesta = AuthService.nuevo_registro(data)
        if int(respuesta)>0:
            return jsonify({'ok': 'Usuario añadido correctamente.'}), 200
        else:
            return False, 201
    except Exception as e:
        print("Error al registrar nuevo usuario. " + e)
        return jsonify({'error': 'Ocurrió un error inesperado al registrar nuevo usuario.'}), 500

