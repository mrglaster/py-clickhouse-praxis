from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class Contractor():
    _id: str = ""
    _parent : str = ""
    _name: str = ""
    _description: str = ""

    def get_json(self):
        return self.to_json()
    
    def parse_json(self, json_data):
        return self.from_json(json_data)
