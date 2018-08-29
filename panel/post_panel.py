from src.panel import Panel
from src.uidefinition import UIDefinition


class PostPanel2(Panel):
    definition = UIDefinition().root('body div:nth-child(2)', 'post2') \
        .with_descendant('h2', 'title') \
        .with_descendant('input', 'input') \
        .with_descendant('li:nth-child(1)', 'comment1') \
        .with_descendant('li:nth-child(2)', 'comment2') \
        .with_descendant('li:nth-child(3)', 'comment3')

    def __init__(self):
        super(PostPanel2, self).__init__()


class PostPanel1(Panel):
    definition = UIDefinition().root('body div:nth-child(1)', 'post1') \
        .with_descendant('h2', 'title') \
        .with_descendant('input', 'input') \
        .with_descendant('li:nth-child(1)', 'comment1') \
        .with_descendant('li:nth-child(2)', 'comment2') \
        .with_descendant('li:nth-child(3)', 'comment3')\
        .with_descendant('a', 'link')


    def __init__(self):
        super(PostPanel1, self).__init__()



