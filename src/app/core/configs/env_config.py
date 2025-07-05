# app/config/env_config.py
import os
import random
from typing import List

from dotenv import load_dotenv

from app.core.configs.base_config import BaseConfig

class EnvSettings:
    pass 
class EnvConfig(BaseConfig):
    def __init__(self):
        load_dotenv() 
        self.settings = EnvSettings()

    def get_api_key(self) -> str:
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise EnvironmentError("LLM_API_KEY environment variable is not set")
        return api_key
    