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

        # Print a specific list
        if args.list:
            result = None
            for list in self._lists:
                if list.is_named(args.list):
                    result = list

            if result:
                result.display(args.desc)
            else:
                print('No list named \'' + args.list + '\' exists.')

        # Print a list of the initialized lists
        else:
            lists = YAML.load('~/.todo/lists.yml')

            print('Initialized Lists')
            print('-----------------')
            for list in lists:
                print(list)

    def remove(self, args):
        print('REMOVE LIST ->', args.list)
        print(args)

    def _choose_adapter(self):
        adapter = YamlAdapter()
        return adapter
