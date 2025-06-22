import pytest
from app.main import app  
from app.routes.ner_routes import ner_bp

@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.register_blueprint(ner_bp, url_prefix='/ner') 
    with app.test_client() as client:
        yield client
