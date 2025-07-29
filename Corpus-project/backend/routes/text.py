from flask import Blueprint, request, jsonify
from database import insert_submission

text_bp = Blueprint('text_bp', __name__)

@text_bp.route('/submit', methods=['POST'])
def submit_text():
    content = request.json
    language = content.get('language')
    text = content.get('text')
    
    if not language or not text:
        return jsonify({'error': 'Missing language or text'}), 400

    insert_submission(('text', language, text, None, None, None))
    return jsonify({'message': 'Text submitted successfully'})
