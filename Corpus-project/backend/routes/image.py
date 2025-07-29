from flask import Blueprint, request, jsonify
import os
from werkzeug.utils import secure_filename
from database import insert_submission

image_bp = Blueprint('image_bp', __name__)

@image_bp.route('/submit', methods=['POST'])
def submit_image():
    caption = request.form.get('caption')
    language = request.form.get('language')
    image = request.files.get('image')

    if not caption or not language or not image:
        return jsonify({'error': 'Missing caption, language, or image'}), 400

    filename = secure_filename(image.filename)
    save_path = os.path.join('uploads/images', filename)
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    image.save(save_path)

    insert_submission(('image', language, None, None, save_path, caption))
    return jsonify({'message': 'Image uploaded successfully'})
