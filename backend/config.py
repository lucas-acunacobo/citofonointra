import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

# Carga las variables de entorno del archivo .env
load_dotenv()

class Config:
    """Clase de configuración de la aplicación."""
    # URI de la base de datos, usando variables de entorno con valores por defecto
    DB_USER = os.environ.get('DB_USER', 'root')
    DB_PASSWORD = os.environ.get('DB_PASSWORD', 'tu-contraseña-segura')
    DB_HOST = os.environ.get('DB_HOST', 'localhost')
    DB_NAME = os.environ.get('DB_NAME', 'citofono_intra')

    SQLALCHEMY_DATABASE_URI = (
        f'mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'una-clave-secreta-muy-larga-y-aleatoria')

    @staticmethod
    def test_connection():
        """
        Método estático para probar la conexión a la base de datos.
        Devuelve True si la conexión es exitosa, False en caso contrario.
        """
        try:
            engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
            with engine.connect():
                print("Conexión a la base de datos exitosa!")
                return True
        except SQLAlchemyError as e:
            print(f"Error al conectar a la base de datos: {e}")
            return False