from dataclasses import dataclass
import string


@dataclass 
class NamedEntity: 
    text :string 
    type: string 
    