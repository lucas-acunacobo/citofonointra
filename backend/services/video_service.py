from flask import Response
import io
from db import db
from modelos.grabacionModel import Grabacion

class VideoService:

    @staticmethod
    def guardarVideo(usuario_id, archivo):
        blob_data = archivo.read()

        nueva_grabacion = Grabacion(
            usuario_id=usuario_id,
            archivo=blob_data
        )
        db.session.add(nueva_grabacion)
        db.session.commit()
        print("Video guardado correctamente:", nueva_grabacion)

    @staticmethod
    def obtener_videos_usuario(usuario_id):
        try:
            grabaciones = Grabacion.query.filter_by(usuario_id=usuario_id).all()
            return [
                {
                    "id": g.id,
                    "usuario_id": g.usuario_id,
                    "creado_en": g.creado_en.strftime("%Y-%m-%d %H:%M:%S")
                }
                for g in grabaciones
            ]
        except Exception as e:
            print("Error al obtener videos:", e)
            return []

    @staticmethod
    def obtenerVideo(id):
        try:
            video = Grabacion.query.get(id)
            if not video:
                return {"error": "No se encontró el video"}, 404
            return Response(
                io.BytesIO(video.archivo),
                mimetype="video/webm",
                direct_passthrough=True
            )
        except Exception as e:
            print("Error al obtener el video:", e)
            return []