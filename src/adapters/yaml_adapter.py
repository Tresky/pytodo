from src.yaml import YAML
from src.adapters.storage_adapter import StorageAdapter
from src.todo_list import TodoList

class YamlAdapter(StorageAdapter):
    def load_list(self, list):
        print('Loading YAML List')
        return TodoList(YAML.load('~/.todo/testlist.yml'))

    def store_list(self, list_obj):
        print('Storing YAML List')
