from __init__ import create_app
from db import db
from modelos.usuarioModel import User
from modelos.grabacionModel import Grabacion

# Crea la app
app = create_app()

# Crea las tablas dentro del contexto de la app
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)