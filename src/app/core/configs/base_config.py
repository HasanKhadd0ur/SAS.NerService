from abc import ABC, abstractmethod
from typing import List

class BaseConfig(ABC):
    def get_api_key(self)->str:
        pass
    