class TodoItem:
    def __init__(self, yaml):
        self._task = yaml['task']
        self._description = yaml['description']
        self._finished = yaml['finished']

    def package_data(self):
        return {
            'task': self._task,
            'description': self._description,
            'finished': self._finished
        }

    def display(self, idx, show_desc):
        print(str(idx) + '. [' + ('x' if self._finished else ' ') + '] ' + self._task)
        if show_desc:
            print('\t-', self._description)
