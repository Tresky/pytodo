class TodoList:
    todos = []

    def __init__(self):
        print('CONSTRUCTING TodoList')

    def display(self, show_desc):
        print('Printing List')
        for i, item in enumerate(todos):
            item.display(i, show_desc)
