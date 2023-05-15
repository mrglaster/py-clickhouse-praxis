from modules.models.building import Building
from modules.models.executor import Executor
from modules.models.act import Act
from modules.service.repository import repo
def main():
    pass



if __name__ == '__main__':
    _repo = repo.create()
    result = _repo.get_acts_json()["acts"][0]
    act = Act().parse_json(result)
    print(act.get_json())
    main()