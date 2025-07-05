from typing import Type, Dict
from app.core.services.NER.ner_service_base import NERService

class ServicesRegistry:
    _ner_service: Dict[str, Type[NERService]] = {}

    @classmethod
    def register_ner_service(cls, name: str, service_cls: Type[NERService]):
        cls._ner_service[name] = service_cls
    
    @classmethod
    def get_ner_service(cls, name: str, *args, **kwargs) -> NERService:
        if name not in cls._ner_service:
            raise ValueError(f"NER Service '{name}' not registered.")
        return cls._ner_service[name](*args, **kwargs)
