from flask import request, jsonify, current_app
from . import file_service


@current_app.route('/fetch_file', methods=['POST'])
def fetch_file():
    data = request.json
    file_id = data.get('file_id')
    
    
    try:
        file_content = file_service.get_file(file_id)
        return jsonify(file_content)
    except Exception as e:
        return jsonify({'error': str(e)}), 500