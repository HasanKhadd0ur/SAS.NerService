from flask import Flask
from app.routes.ner_routes import ner_bp


def create_app():
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(ner_bp, url_prefix="/ner")

    print("\n📍 Registered Routes:")
    for rule in app.url_map.iter_rules():
        print(f"{rule.endpoint:25s} -> {rule.methods} {rule.rule}")


    return app
