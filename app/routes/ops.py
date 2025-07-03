from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.utils import secure_filename
import os

ops_bp = Blueprint('ops', __name__)
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pptx', 'docx', 'xlsx'}

def allowed(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@ops_bp.route('/upload', methods=['POST'])
@jwt_required()
def upload_file():
    identity = get_jwt_identity()
    if identity['role'] != 'ops':
        return jsonify({"msg": "Unauthorized"}), 403

    if 'file' not in request.files:
        return jsonify({"msg": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"msg": "No selected file"}), 400

    if file and allowed(file.filename):
        filename = secure_filename(file.filename)
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)
        return jsonify({"msg": "File uploaded successfully", "file": filename})
    return jsonify({"msg": "Invalid file type"}), 400