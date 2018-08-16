from src.panle import Panel
from src.uidefinition import UIdefinition


class TodoApp(Panel):

    def __init__(self, browser_name):
        super(TodoApp, self).__init__(browser_name)
        self.definition = UIdefinition.root('test', 'test')\
            .withdescendant('test').\
            withdescendant('test2').\
            withdescendant('test3')


if __name__ == "__main__":
    todo = TodoApp('chrome')
    print(todo.definition.descendant)
