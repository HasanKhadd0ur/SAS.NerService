from flask import Blueprint, request, jsonify
from app.core.factory.services_factory import get_ner_service
from app.core.factory.services_registry import ServicesRegistry


ner_bp = Blueprint('ner', __name__)

ner_service = get_ner_service("stanza")

@ner_bp.route('/extract', methods=['POST'])
def extract():
    data = request.get_data(as_text=True)
    result = ner_service.extract_ner(data)
    return jsonify(result)
