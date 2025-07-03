from flask import Flask
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from dotenv import load_dotenv
import os

mongo = PyMongo()
jwt = JWTManager()

def create_app():
    load_dotenv()
    app = Flask(__name__)
    CORS(app)

    app.config['MONGO_URI'] = os.getenv('MONGO_URI')
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET')

    mongo.init_app(app)
    jwt.init_app(app)

    from app.routes.auth import auth_bp
    from app.routes.ops import ops_bp
    from app.routes.client import client_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(ops_bp, url_prefix='/ops')
    app.register_blueprint(client_bp, url_prefix='/client')

    return app