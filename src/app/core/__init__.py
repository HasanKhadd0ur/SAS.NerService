from app.core.factory.services_registry import ServicesRegistry
from app.core.services.NER.stanza_ner_service import StanzaNERService


ServicesRegistry.register_ner_service('stanza',StanzaNERService)
