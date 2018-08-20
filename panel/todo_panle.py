from src.panle import Panel
from src.uidefinition import UIDefinition


class AndPanel(Panel):
    definition = UIDefinition.root('div.add', 'and') \
        .withdescendant('div.and1', 'and1') \
        .withdescendant('div.and2', 'and2') \
        .withdescendant('div.and3')
    def __init__(self):
        super(AndPanel, self).__init__()


class TestPanel(Panel):

    definition = UIDefinition.root('test', 'test') \
        .withdescendant('test') \
        .withdescendant('test2') \
        .withdescendant('test3') \
        .withdescendant(AndPanel)

    def __init__(self):
        super(TestPanel, self).__init__()


class TodoApp(Panel):

    definition = UIDefinition.root('div.app', 'app') \
        .withdescendant('div.sa') \
        .withdescendant('div.cd') \
        .withdescendant('div.wd') \
        .withdescendant(TestPanel)

    def __init__(self):
        super(TodoApp, self).__init__()






