from abc import abstractmethod
from typing import List
from app.core.configs.base_config import BaseConfig
from app.core.models.named_entity import NamedEntity


class NERService:
    
    def __init__(self,config :BaseConfig):
        self.config =config

    @abstractmethod    
    def extract_ner(self, text: str) -> List[NamedEntity]:
        pass