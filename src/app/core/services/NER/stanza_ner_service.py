from app.core.services.NER.ner_service_base import NERService
from app.core.configs.base_config import BaseConfig
from app.core.models.named_entity import NamedEntity
from typing import List
import stanza


class StanzaNERService(NERService):
    # Static flag to avoid repeated setup
    _pipeline_initialized = False 
    
    def __init__(self, config: BaseConfig):
        try:
            if not StanzaNERService._pipeline_initialized:
                # Download the Arabic models if not already downloaded
                stanza.download('ar', processors='tokenize,ner', verbose=False)
                StanzaNERService._pipeline_initialized = True

            # Initialize the Stanza pipeline
            self.nlp = stanza.Pipeline(lang='ar', processors='tokenize,ner', use_gpu=False)
        except Exception as e:
            raise RuntimeError(f"Failed to load Stanza NER pipeline: {e}")

    def extract_ner(self, text: str) -> List[NamedEntity]:
        try:
            doc = self.nlp(text)
            entities: List[NamedEntity] = []

            for sentence in doc.sentences:
                for entity in sentence.ents:
                    # Filter out entities with type "OTHER"
                    if entity.type != "OTHER":
                        entities.append(NamedEntity(entity.text, entity.type))

            return entities
        except Exception as e:
            raise RuntimeError(f"NER location extraction failed: {e}")
