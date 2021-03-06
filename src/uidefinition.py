class UIDefinition:

    def __init__(self):
        self.descendant = list()
        self.selector = None
        self.name = None

    def root(self, selector, name=None):
        self.selector = selector
        self.name = name
        return self

    def with_descendant(self, selector_or_constructor, name=None):
        self.descendant.append([selector_or_constructor, name])
        return self

    def find_ui_node(self, name):
        for node in self.walk_ui_node():
            if node['name'] == name:
                return node

    def walk_ui_node(self):
        has_descendant = len(self.descendant) > 0
        yield {
            'selector': self.selector,
            'name': self.name,
            'has_descendant': has_descendant
        }
        for selector_or_constructor, name in self.descendant:
            if isinstance(selector_or_constructor, str):
                yield {
                    'selector': ' '.join([self.selector, selector_or_constructor]),
                    'name': name,
                    'has_descendant': False
                }
            else:
                definition = selector_or_constructor.definition
                nodes = definition.walk_ui_node()
                if name:
                    node = nodes.__next__()
                    yield {
                        'selector': ' '.join([self.selector, node['selector']]),
                        'name': name,
                        'has_descendant': node['has_descendant']
                    }
                for node in nodes:
                    node['selector'] = ' '.join([self.selector, node['selector']])
                    yield node


class UINode:

    def __init__(self, selector, name, has_descendants):
        self.selector = selector
        self.name = name
        self.has_descendants = has_descendants


class Descendant:

    def __init__(self, selector, name):
        self.selector = selector
        self.name = name
