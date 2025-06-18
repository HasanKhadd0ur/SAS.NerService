from dataclasses import dataclass
import string


@dataclass 
class NamedEntity: 
    entity_name :string 
    type: string 
    