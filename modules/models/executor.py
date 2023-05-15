from dataclasses import dataclass
from modules.models.contractor import Contractor
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class Executor():
    _id : str = ""
    _name: str = ""
    _description : str = ""
    _contractor : Contractor = None

    def get_json(self):
        return self.to_json()
    
    def parse_json(self, json_data):
        return self.from_json(json_data)