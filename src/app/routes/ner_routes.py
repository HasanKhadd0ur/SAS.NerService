from flask import Blueprint, request, jsonify

from app.core.services.ner_service import NERService

ner_bp = Blueprint('ner', __name__)


ner_service = NERService()
@ner_bp.route('/extract', methods=['POST'])
def extract():
    data = request.get_data()
    result = ner_service.extract_ner(data)
    return jsonify(result)