from flask_sqlalchemy import SQLAlchemy

# Instancia de SQLAlchemy, inicializada más tarde
db = SQLAlchemy()

class User(db.Model):
    """Modelo de la tabla de usuarios."""
    __tablename__ = 'usuario'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido_paterno = db.Column(db.String(50), nullable=False)
    apellido_materno = db.Column(db.String(50), nullable=False)
    clave = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    creado_en = db.Column(db.TIMESTAMP, default=db.func.current_timestamp())

    def __repr__(self):
        return f"<User {self.nombre} {self.apellido_paterno} {self.apellido_materno}>"
