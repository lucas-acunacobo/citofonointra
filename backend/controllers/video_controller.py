from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from services.video_service import VideoService

video_bp = Blueprint('video', __name__, url_prefix='/video')

@video_bp.route('/guardarvideo', methods=['POST'])
@cross_origin()
def guardarVideo():
    try:
        archivo = request.files.get('video')
        usuario_id = request.form.get('usuarioId')

        if not archivo:
            return jsonify({'error': 'Falta el archivo'}), 400
        if not usuario_id:
            return jsonify({'error': 'Falta el id'}), 400

        VideoService.guardarVideo(usuario_id, archivo)
        return jsonify({'ok': True})
    except Exception as e:
        print("Error al guardar video:", str(e))
        return jsonify({'error': 'Ocurrió un error inesperado.'}), 500

@video_bp.route('/obtenervideousuario', methods=['POST'])
@cross_origin()
def obtenerVideoUsuario():
    data = request.get_json()
    try:
        userid = data.get('userid')
        videos = VideoService.obtener_videos_usuario(userid)
        return jsonify(videos), 200

    except Exception as e:
        print("Error al obtener video:", str(e))
        return jsonify({'error': 'Ocurrió un error inesperado.'}), 500

@video_bp.route('/obtenerVideo', methods=['POST'])
@cross_origin()
def obtenerVideo():
    data = request.get_json()
    try:
        videoid = data.get('videoid')
        video = VideoService.obtenerVideo(videoid)
        return video, 200

    except Exception as e:
        print("Error al cargar video:", str(e))
        return jsonify({'error': 'Ocurrió un error inesperado.'}), 500