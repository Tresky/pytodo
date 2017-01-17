import yaml

class TodoRoot:
    config = yaml.load(open('./config.yml', 'r'))
    lists = []

    def __init__(self):
        print('CONSTRUCTING TodoRoot')
        print(self.config)

        # Load the list(s) into memory
        # adapter = chooseAdapter()
        # adapter.loadAllLists()
        # adapter.loadList('testlist')

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
