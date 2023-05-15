from dataclasses import dataclass
from modules.models.executor import Executor
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class Building():
    _id: str = ""
    _name: str = ""
    _description: str = ""
    _executor: Executor = None
    
    def get_json(self):
        return self.to_json()
    
    def parse_json(self, json_data):
        return self.from_json(json_data)