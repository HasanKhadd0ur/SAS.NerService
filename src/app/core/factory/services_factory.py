from app.core.configs.env_config import EnvConfig
from app.core.factory.services_registry import ServicesRegistry

config = EnvConfig()
   
def get_ner_service(key : str ):

    return ServicesRegistry.get_ner_service(key,config)
