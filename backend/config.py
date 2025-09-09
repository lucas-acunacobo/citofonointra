import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DB_USER = os.environ.get('DB_USER', 'root')
    DB_PASSWORD = os.environ.get('DB_PASSWORD', 'tu-contraseña-segura')
    DB_HOST = os.environ.get('DB_HOST', 'localhost')
    DB_NAME = os.environ.get('DB_NAME', 'citofono_intra')
    DB_PORT = os.environ.get('DB_PORT', '5432')

    #SQLALCHEMY_DATABASE_URI = (
    #    f'postgresql://citofono_intra_user:oaJ2PKm6SHk5N34pO1jnIRWuBgwZjOCl@dpg-d2uh706r433s73ea2l20-a.oregon-postgres.render.com/citofono_intra'
    #)
    SQLALCHEMY_DATABASE_URI = (
        f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
"""
    cod desarrollo
    SQLALCHEMY_DATABASE_URI = (
        f'mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
"""
