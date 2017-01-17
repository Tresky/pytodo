from src.todo_item import TodoItem

class TodoList:
    _name = ''
    _todos = []

    def __init__(self, yaml):
        self._name = yaml['name']
        for task in yaml['tasks']:
            self._todos.append(TodoItem(task))

    def is_named(self, name):
        return self._name == name

    def display(self, show_desc):
        for i, item in enumerate(self._todos):
            item.display(i, show_desc)
