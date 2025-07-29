from flask import Blueprint, request, jsonify
import os
from werkzeug.utils import secure_filename
from database import insert_submission

audio_bp = Blueprint('audio_bp', __name__)

@audio_bp.route('/submit', methods=['POST'])
def submit_audio():
    language = request.form.get('language')
    audio = request.files.get('audio')

    if not language or not audio:
        return jsonify({'error': 'Missing language or audio file'}), 400

    filename = secure_filename(audio.filename)
    save_path = os.path.join('uploads/audio', filename)
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    audio.save(save_path)

    insert_submission(('audio', language, None, save_path, None, None))
    return jsonify({'message': 'Audio uploaded successfully'})
