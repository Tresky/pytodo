from src.utils.yaml import YAML
from src.storage_adapters.yaml_adapter import YamlAdapter
from src.todo_list import TodoList

# @class TodoRoot
# @desc Root level class that represents the entirety of the
# application. This has functions that are called from the
# argument parser to handle the subcommands in the CLI tool.
class TodoRoot:
    _config = YAML.load('./config.yml')

    # Constructor: Set the default values for the instance
    def __init__(self):
        # Load the list(s) into memory
        self._adapter = self._choose_storage_adapter()
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

    # Subcommand: Initialize an empty list with a given name.
    # @param args Object of the arguments being passed in from the CLI
    def init(self, args):
        # Check if list exists with given name
        if self._find_list(args.list) == None:
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

    # Subcommand: Add a task to a specified list.
    # @param args Object of the arguments being passed in from the CLI
    def add(self, args):
        list = self._get_list(args.list)
        if list:
            list.add_todo(args.task, 'New Description :]')

            self._changed = True

            ## Temporary; see __del__
            self._adapter.store_lists(self._lists)
        else:
            print('No list named \'' + args.list + '\' exists.')

    # Subcommand: Display a list of the lists present or the tasks in a list.
    # @param args Object of the arguments being passed in from the CLI
    def list(self, args):
        # Print a specific list
        if args.list:
            result = self._get_list(args.list)

            if result:
                result.display(args.d)
            else:
                print('No list named \'' + args.list + '\' exists.')

        # Print a list of the initialized lists
        else:
            lists = YAML.load('~/.todo/lists.yml')

            print('Initialized Lists')
            print('-----------------')
            for list in lists:
                print(list)

    # Subcommand: Remove an entire list or a task from a list.
    # @param args Object of the arguments being passed in from the CLI
    def remove(self, args):
        ##! Need to make this actually delete the file
        ##! associated with the todo list, too

        if not args.item:
            index = self._find_list(args.list)
            if index:
                self._lists.pop(index)
        else:
            result = self._get_list(args.list)
            result.remove_todo(args.item)

        ## Temporary; see __del__
        self._adapter.store_lists(self._lists)

    # Subcommand: Mark a task as finished in a specific list.
    # @param args Object of the arguments being passed in from the CLI
    def finish(self, args):
        if args.list:
            result = self._get_list(args.list)

            func = (result.finish_task if not args.u else result.unfinish_task)
            func(args.task_idx)

            ## Temporary; see __del__
            self._adapter.store_lists(self._lists)

    # Discover which storage adapter to use based on settings.
    # @return Object instance of the correct storage adapter
    def _choose_storage_adapter(self):
        adapter = YamlAdapter()
        return adapter

    # Retrieve a list based on the name of the list.
    # @param list_name Name of the list to retrieve
    # @return Returns the list object if found, None otherwise
    def _get_list(self, list_name):
        result = None
        for l in self._lists:
            if l.is_named(list_name):
                result = l
        return result

    # Retrieve the index of a list based on the name of the list.
    # @param list_name Name of the list to find
    # @return Return the index of the list if found, None otherwise
    def _find_list(self, list_name):
        index = None
        for idx, l in enumerate(self._lists):
            if l.is_named(list_name):
                index = idx
        return index
