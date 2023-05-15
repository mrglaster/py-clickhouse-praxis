import unittest
from ..modules.service.repository import repo

class reposity_tests(unittest.TestCase):
    # Проверить получение актов
    def test_get_acts(self):
        # Подготовка
        _repo = repo.create()
        

        # Действие
        result = _repo.get_acts()

        # Проверки
        assert len(result) > 0
        print(result)