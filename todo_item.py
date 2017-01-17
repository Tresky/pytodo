class TodoItem:
    task = ''
    description = ''
    finished = False

    def __init__(self, obj):
        print('CONSTRUCTING TodoItem')
        self.task = obj.task
        self.description = obj.description
        self.finished = obj.finished

    def display(self, idx, show_desc):
        print(idx + '. [' + ('x' if self.finished else ' ') + ']' + self.task)
        if show_desc:
            print('\t-', self.description)
