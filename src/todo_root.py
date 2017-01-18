from src.yaml import YAML
from src.adapters.yaml_adapter import YamlAdapter
from src.todo_list import TodoList

class TodoRoot:
    _config = YAML.load('./config.yml')

    def __init__(self):
        # Load the list(s) into memory
        self._adapter = self._choose_adapter()
        self._lists = self._adapter.load_all_lists()
        self._changed = False

    # def __del__(self):
        # If there are any changes to be saved, save them
        # This code doesn't work. Due to a change in Python3,
        # you can no longer use open() to open files in the __del__
        # function. So, this need to be fixed.
        # For now, these two lines will be placed in each function
        # individually.
        # if self._changed:
            # self._adapter.store_lists(self._lists)

    def init(self, args):
        print('INITIALIZE ->', args.list)
        print(args)

        # Check if list exists with given name
        already_exists = False
        for list in self._lists:
            if list.is_named(args.list):
                already_exists = True
                break
        if already_exists:
            print('List with name \'' + args.list + '\' already exists.')
            return

        # Template YAML for making a new list
        raw = '''
            'name': {name}
            'tasks': []
        '''.format(name=args.list)

        # The new list is only added into memory.
        # Will be saved by storage adapters later
        self._lists.append(TodoList(YAML.parse_yaml(raw)))
        self._changed = True

        ## Temporary; see __del__
        self._adapter.store_lists(self._lists)

    def add(self, args):
        print('ADD TASK ->', args.list, ':', args.task)
        print(args)

        list = self._find_list(args.list)
        if list:
            list.add_todo(args.task, 'new description :)')

            self._changed = True

            ## Temporary; see __del__
            self._adapter.store_lists(self._lists)
        else:
            print('No list named \'' + args.list + '\' exists.')

    def list(self, args):
        print('SHOW LIST ->', args.list)
        print(args)

        # Print a specific list
        if args.list:
            result = self._find_list(args.list)

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

        ##! Need to make this actually delete the file
        ##! associated with the todo list, too

        if not args.item:
            index = self._find_list_index(args.list)
            if index:
                self._lists.pop(index)
        else:
            result = self._find_list(args.list)
            result.remove_todo(args.item)

        ## Temporary; see __del__
        self._adapter.store_lists(self._lists)

    def _choose_adapter(self):
        adapter = YamlAdapter()
        return adapter

    def _find_list(self, list_name):
        result = None
        for l in self._lists:
            if l.is_named(list_name):
                result = l
        return result

    def _find_list_index(self, list_name):
        index = None
        for idx, l in enumerate(self._lists):
            if l.is_named(list_name):
                index = idx
        return index
