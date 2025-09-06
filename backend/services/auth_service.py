import base64

from werkzeug.security import generate_password_hash, check_password_hash
from db import db
from modelos.grabacionModel import Grabacion
from modelos.usuarioModel import User


class AuthService:
    @staticmethod
    def hash_password(password):
        return generate_password_hash(password)

    @staticmethod
    def check_password(hashed_password, password):
        return check_password_hash(hashed_password, password)

    @staticmethod
    def validar_usuario(email, password):
        clean_email = email.strip().lower()

        user = User.query.filter_by(email=clean_email).first()

        if not user:
            return None

        if not check_password_hash(user.clave, password):
            return None

        return user

    @staticmethod
    def obtener_usuarios():
        users = User.query.all()
        users_list = []

        for user in users:
            users_list.append({
            'id': user.id,
            'nombre': user.nombre,
            'apellido_paterno': user.apellido_paterno,
            'apellido_materno': user.apellido_materno,
            'email': user.email,
            'creado_en': user.creado_en.strftime('%Y-%m-%d %H:%M:%S')
        })
        return users_list