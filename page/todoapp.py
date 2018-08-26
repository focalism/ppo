from panel.todo_panle import TodoApp
from src.page import Page


class TodoPage(Page):
    init_panels = [TodoApp]
    url = None

    def __init__(self):
        super(TodoPage, self).__init__()


