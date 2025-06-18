from flask import Flask
from app.routes.ner_routes import ner_bp


def create_app():
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(ner_bp, url_prefix="/ner")

    return app
