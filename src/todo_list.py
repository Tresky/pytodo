from src.todo_item import TodoItem

class TodoList:
    _name = ''
    _todos = []

    def __init__(self, yaml):
        self._name = yaml['name']
        for task in yaml['tasks']:
            self._todos.append(TodoItem(task))
    def package_data(self):
        data = {
            'name': self._name,
            'tasks': []
        }

        for todo in self._todos:
            data['tasks'].append(todo.package_data())

        return data

    def is_named(self, name):
        return self._name == name

    def display(self, show_desc):
        for i, item in enumerate(self._todos):
            item.display(i, show_desc)
