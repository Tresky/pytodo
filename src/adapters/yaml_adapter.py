from src.yaml import YAML
from src.adapters.storage_adapter import StorageAdapter
from src.todo_list import TodoList

class YamlAdapter(StorageAdapter):
    def load_all_lists(self):
        lists_file = YAML.load('~/.todo/lists.yml')

        lists = []
        for list in lists_file:
            lists.append(self.load_list(list))
        return lists

    def load_list(self, list):
        print('Loading YAML List', list)
        return TodoList(YAML.load('~/.todo/' + list + '.yml'))

    def store_lists(self, lists):
        list_names = []
        for list in lists:
            list_names.append(list._name)
            self.store_list(list)

        YAML.write('~/.todo/lists.yml', list_names)

    def store_list(self, list):
        print('Storing List:', list._name)
        YAML.write('~/.todo/' + list._name + '.yml', list.package_data())
