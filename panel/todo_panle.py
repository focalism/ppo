from src.panel import Panel
from src.uidefinition import UIDefinition


class AndPanel(Panel):
    definition = UIDefinition().root('div.add', 'and') \
        .with_descendant('div.and1', 'and1') \
        .with_descendant('div.and2', 'and2') \
        .with_descendant('div.and3')


class TestPanel(Panel):

    definition = UIDefinition().root('test', 'test') \
        .with_descendant('test') \
        .with_descendant('test2') \
        .with_descendant('test3') \
        .with_descendant(AndPanel)


class TodoApp(Panel):

    definition = UIDefinition().root('div.app', 'app') \
        .with_descendant('div.sa', 'title') \
        .with_descendant('div.cd') \
        .with_descendant('div.wd') \
        .with_descendant(TestPanel, 'post_panel2')







