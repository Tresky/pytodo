from src.todo_item import TodoItem

# @class TodoList
# @desc Represents a single todo list that stores multiple
# tasks. Contains a name and a list of TodoItem objects.
class TodoList:
    def __init__(self, yaml):
        self._name = yaml['name']
        self._todos = []
        if yaml['tasks']:
            for task in yaml['tasks']:
                self._todos.append(TodoItem(task))
        else:
            self._todos = []

    # Adds a task item to the in-memory list.
    # @param task Text of the task to add
    # @param description Text of the description to add
    def add_todo(self, task, description):
        todo = {
            'task': task,
            'description': description,
            'finished': False
        }
        self._todos.append(TodoItem(todo))

    # Remove a task item from the list based on index.
    # @param index Index of the task to remove
    def remove_todo(self, index):
        self._todos.pop(index)

    # Mark a task as 'finished' based on index.
    # @param index Index of the task to mark 'finished'
    def finish_task(self, index):
        self._todos[index].finish()

    # Mark a task as 'unfinished' based on index.
    # @param index Index of the task to mark 'unfinished'
    def unfinish_task(self, index):
        self._todos[index].unfinish()

    # Package all of the list's data into an object
    # representation to be converted to YAML.
    def package_data(self):
        data = {
            'name': self._name,
            'tasks': []
        }

        for todo in self._todos:
            data['tasks'].append(todo.package_data())

        return data

    # Returns whether or not the list is named a
    # certain thing.
    # @param name Name to compare with against
    # @return True if list is named based on param, false otherwise
    def is_named(self, name):
        return self._name == name

    # Display the entire formatted list contents to the terminal.
    # @param show_desc True if descriptions should be shown, false otherwise
    def display(self, show_desc):
        print('Todos for \'{name}\''.format(name=self._name))
        if len(self._todos):
            for i, item in enumerate(self._todos):
                item.display(i, show_desc)
        else:
            print('No tasks in this list.')
