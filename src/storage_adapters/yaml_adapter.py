from src.utils.yaml import YAML
from src.storage_adapters.storage_adapter import StorageAdapter
from src.todo_list import TodoList
from src.utils.logger import Logger

class YamlAdapter(StorageAdapter):
    def load_all_lists(self):
        Logger.debug('Loading YAML lists')
        lists_file = YAML.load('~/.todo/lists.yml')

        lists = []
        for list in lists_file:
            lists.append(self.load_list(list))
        return lists

    def load_list(self, list):
        return TodoList(YAML.load('~/.todo/' + list + '.yml'))

    def store_lists(self, lists):
        Logger.debug('Storing YAML lists')
        list_names = []
        for list in lists:
            list_names.append(list._name)
            self.store_list(list)

        YAML.write('~/.todo/lists.yml', list_names)

    def store_list(self, list):
        YAML.write('~/.todo/' + list._name + '.yml', list.package_data())
