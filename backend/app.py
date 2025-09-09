from __init__ import create_app
from db import db
from modelos.usuarioModel import User
from modelos.grabacionModel import Grabacion

app = create_app()

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)