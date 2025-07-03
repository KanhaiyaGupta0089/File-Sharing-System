from flask import Blueprint, request, jsonify
from app import mongo
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = mongo.db.users.find_one({"email": data['email'], "password": data['password']})
    if not user:
        return jsonify({"msg": "Invalid credentials"}), 401

    token = create_access_token(identity={"email": user['email'], "role": user['role']})
    return jsonify({"token": token, "role": user['role']})