from flask import Flask
from flask_cors import CORS
from .routes import register_routes
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app, origins="*", methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])

    register_routes(app)
    return app
