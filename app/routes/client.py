from flask import Blueprint, request, jsonify, send_file
from app import mongo
from flask_jwt_extended import jwt_required, get_jwt_identity
import os
from itsdangerous import URLSafeSerializer

client_bp = Blueprint('client', __name__)
serializer = URLSafeSerializer('SECRET!')

@client_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    mongo.db.users.insert_one({
        'email': data['email'],
        'password': data['password'],
        'role': 'client'
    })
    token = serializer.dumps(data['email'])
    encrypted_url = f'/client/verify/{token}'
    return jsonify({'url': encrypted_url})

@client_bp.route('/verify/<token>', methods=['GET'])
def verify_email(token):
    try:
        email = serializer.loads(token)
        return jsonify({'msg': f'{email} verified successfully'})
    except:
        return jsonify({'msg': 'Invalid token'}), 400

@client_bp.route('/files', methods=['GET'])
@jwt_required()
def list_files():
    identity = get_jwt_identity()
    if identity['role'] != 'client':
        return jsonify({"msg": "Unauthorized"}), 403
    files = os.listdir('uploads')
    return jsonify({"files": files})

@client_bp.route('/download-link/<filename>', methods=['GET'])
@jwt_required()
def generate_link(filename):
    identity = get_jwt_identity()
    if identity['role'] != 'client':
        return jsonify({"msg": "Unauthorized"}), 403

    encrypted = serializer.dumps(filename)
    return jsonify({"download-link": f"/client/download/{encrypted}"})

@client_bp.route('/download/<token>', methods=['GET'])
@jwt_required()
def download_file(token):
    identity = get_jwt_identity()
    if identity['role'] != 'client':
        return jsonify({"msg": "Unauthorized"}), 403
    try:
        filename = serializer.loads(token)
        return send_file(f'uploads/{filename}', as_attachment=True)
    except:
        return jsonify({'msg': 'Invalid or expired link'}), 400