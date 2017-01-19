from src.utils.yaml import YAML
from src.storage_adapters.storage_adapter import StorageAdapter
from src.todo_list import TodoList
from src.utils.logger import Logger

# @class YamlAdapter
# @desc YAML-based storage adapter to allow the program
# to interact with YAML files for storage and retrieval.
class YamlAdapter(StorageAdapter):
    # Load all of the lists that are present in the
    # lists.yml file.
    # @return Array of all of the loaded lists
    def load_all_lists(self):
        Logger.debug('Loading YAML lists')
        lists_file = YAML.load('~/.todo/lists.yml')

        lists = []
        for list in lists_file:
            lists.append(self.load_list(list))
        return lists

    # Load a single list with a given name.
    # @param list_name Name of the list to load into memory
    # @return TodoList object of the loaded list
    def load_list(self, list_name):
        return TodoList(YAML.load('~/.todo/' + list_name + '.yml'))

    # Write all passed-in lists to their respective files.
    # @param lists Array of the lists to write
    def store_lists(self, lists):
        Logger.debug('Storing YAML lists')
        list_names = []
        for list in lists:
            list_names.append(list._name)
            self.store_list(list)

        YAML.write('~/.todo/lists.yml', list_names)

    # Write a single, given list to its respective file.
    # @param list TodoList object to write
    def store_list(self, list):
        YAML.write('~/.todo/' + list._name + '.yml', list.package_data())
