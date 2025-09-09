from db import db
from datetime import datetime

class Grabacion(db.Model):
    __tablename__ = "grabacion"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuario.id", ondelete="CASCADE"), nullable=False)
    archivo = db.Column(db.LargeBinary, nullable=False)
    creado_en = db.Column(db.DateTime, default=datetime.utcnow)

    usuario = db.relationship("User", backref=db.backref("grabaciones", lazy=True))
