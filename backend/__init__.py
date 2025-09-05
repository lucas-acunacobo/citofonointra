from flask import Flask
from config import Config
from models import db
from controllers.auth_controller import auth_bp

def create_app():
    """Función de factoría para crear la aplicación Flask."""
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializa la base de datos
    db.init_app(app)

    # Registra los Blueprints de los controladores
    app.register_blueprint(auth_bp)

    return app