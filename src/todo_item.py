# @class TodoItem
# @desc Represents a single todo item in a list. Contains
# the text of the task, the text of the description, and
# a boolean on whether the task is finished or not.
class TodoItem:
    def __init__(self, yaml):
        self._task = yaml['task']
        self._description = yaml['description']
        self._finished = yaml['finished']

    # Package all of the list's data into an object
    # representation to be converted to YAML.
    def package_data(self):
        return {
            'task': self._task,
            'description': self._description,
            'finished': self._finished
        }

    # Mark the item as 'finished'.
    def finish(self):
        self._finished = True

    # Mark the item as 'unfinished'.
    def unfinish(self):
        self._finished = False

    # Display the formatted task to the terminal.
    # @param show_desc True if the description should be shown, false otherwise
    def display(self, idx, show_desc):
        print(str(idx) + '. [' + ('x' if self._finished else ' ') + '] ' + self._task)
        if show_desc:
            print('\t-', self._description)
