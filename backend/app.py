import os
from __init__ import create_app
from werkzeug.security import generate_password_hash
from models import db, User

# Crea una instancia de la aplicación llamando a la función de fábrica
app = create_app()

if __name__ == '__main__':
    with app.app_context():
        # Crea las tablas de la base de datos si no existen
        db.create_all()

        # Opcional: crea un usuario de prueba si no existe
        if not db.session.query(db.exists().where(User.email == 'test@example.com')).scalar():
            hashed_password = generate_password_hash("password123")
            test_user = User(
                nombre='Test',
                apellido_paterno='test',
                apellido_materno='test',
                email='test@example.com',
                clave=hashed_password
            )
            db.session.add(test_user)
            db.session.commit()
            print("Usuario de prueba 'test@example.com' creado.")

    app.run(debug=True)