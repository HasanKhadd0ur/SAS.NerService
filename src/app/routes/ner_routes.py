import logging
from flask import Blueprint, request, jsonify
from app.core.factory.services_factory import get_ner_service

ner_bp = Blueprint('ner', __name__)
ner_service = get_ner_service("stanza")

# Configure logging (you can configure this once in your app's entrypoint instead)
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

@ner_bp.route('/extract', methods=['POST'])
def extract():
    data = request.get_data(as_text=True)
    result = ner_service.extract_ner(data)

    # Log the result
    logger.debug(f"NER Extraction result for input: {data}")
    logger.debug(f"Extracted entities: {result}")

    return jsonify(result)
