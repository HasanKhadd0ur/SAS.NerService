from flask import Flask
from app.routes.ner_routes import ner_bp

app = Flask(__name__)

# Register blueprints
# app.register_blueprint(ner_bp, url_prefix="/ner")
if __name__ == "__main__":
    app.run(debug=True)
    