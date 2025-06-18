from typing import List
import stanza

from app.core.models.named_entity import NamedEntity


class NERService:
    def __init__(self):
        try:
            # Download only once
            stanza.download('ar', processors='tokenize,ner', verbose=False)
            self.nlp = stanza.Pipeline(lang='ar', processors='tokenize,ner', use_gpu=False)
        except Exception as e:
            raise RuntimeError(f"Failed to load Stanza NER pipeline: {e}")

    def extract_ner(self, text: str) -> List[NamedEntity]:
        try:
            doc = self.nlp(text)
            entities :List[NamedEntity] = []

            for sentence in doc.sentences:
                for entity in sentence.ents:
                    entities.append( NamedEntity(entity.text,entity.type))
            return entities
        
        # Return only the first location
        except Exception as e:
            raise RuntimeError(f"NER location extraction failed: {e}")
