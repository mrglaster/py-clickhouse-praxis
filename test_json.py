import unittest
from modules.service.repository import repo
from modules.models.act import Act

class json_tests(unittest.TestCase):
    def test_get_json_acts(self):
        _repo = repo.create()
        act = _repo.get_acts_json()["acts"][0]
        newer_act = Act().parse_json(act).get_json()
        assert act == newer_act
        assert len(act) == len(newer_act)

    