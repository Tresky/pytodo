from src.yaml import YAML
from os.path import expanduser
from src.adapters.yaml_adapter import YamlAdapter

class TodoRoot:
    _config = YAML.load('./config.yml')
    _lists = []

    def __init__(self):
        # Load the list(s) into memory
        self._adapter = self._choose_adapter()
        self._lists = [self._adapter.load_list('testlist')]

    def init(self, args):
        print('INITIALIZE ->', args.list)
        print(args)

    def add(self, args):
        print('ADD TASK ->', args.list, ':', args.task)
        print(args)

    def list(self, args):
        print('SHOW LIST ->', args.list)
        print(args)

    def remove(self, args):
        print('REMOVE LIST ->', args.list)
        print(args)

    def _choose_adapter(self):
        adapter = YamlAdapter()
        return adapter
