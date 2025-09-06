from flask import Flask
from config import Config
from db import db
from controllers.auth_controller import auth_bp
from controllers.video_controller import video_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializa la base de datos
    db.init_app(app)

    # Registra los Blueprints de los controladores
    app.register_blueprint(auth_bp)
    app.register_blueprint(video_bp)

    return app