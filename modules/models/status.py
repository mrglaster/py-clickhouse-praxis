from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class Status():
    _id: str = ""
    _code: int = 0
    _name: str =""
    _description: str= ""

    @property
    def id(self)->str:
        return self._id
    
    @id.setter
    def id(self, id_new:str):
        self._id = id_new
    
    @property
    def code(self):
        return self._code
    
    @code.setter
    def code(self, new_code: int):
        self._code = new_code
    
    @property
    def name(self)->str:
        return self._name
    
    @name.setter
    def name(self, name_new:str):
        self._name = name_new
    
    @property
    def description(self)->str:
        return self._description
    
    @description.setter
    def description(self, new_description):
        self._description = new_description

    def get_json(self):
        return self.to_json()
    
    def parse_json(self, json_data):
        return self.from_json(json_data)