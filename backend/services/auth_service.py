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

    @staticmethod
    def nuevo_registro(data):
        try:
            nombre = data.get('nombre')
            apellido_paterno = data.get('apellido_paterno')
            apellido_materno = data.get('apellido_materno')
            email = data.get('email')
            clave = data.get('clave')
            print(data)
            existing_user = User.query.filter_by(email=email).first()
            if existing_user:
                return 0

            hashed_password = generate_password_hash(clave)

            new_user = User(
                nombre=nombre,
                apellido_paterno=apellido_paterno,
                apellido_materno=apellido_materno,
                clave=hashed_password,
                email=email
            )
            db.session.add(new_user)
            db.session.commit()

            return new_user.id
        except Exception as e:
            db.session.rollback()
            return 0

