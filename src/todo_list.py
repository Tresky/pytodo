from src.todo_item import TodoItem

class TodoList:
    def __init__(self, yaml):
        self._name = yaml['name']
        self._todos = []
        if yaml['tasks']:
            for task in yaml['tasks']:
                self._todos.append(TodoItem(task))
        else:
            self._todos = []

    def add_todo(self, task, description):
        todo = {
            'task': task,
            'description': description,
            'finished': False
        }
        self._todos.append(TodoItem(todo))

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
        if len(self._todos):
            for i, item in enumerate(self._todos):
                item.display(i, show_desc)
        else:
            print('No tasks in this list.')
