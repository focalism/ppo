class UIdefinition():

    def __init__(self, selector, name):
        self.selector = selector
        self.name = name
        self.descendant = list()

    def root(self, selector, name=None):
        return UIdefinition(selector, name)

    def withdescendant(self, selector_or_construactor, name=None):
        self.descendant.append([selector_or_construactor, name])
        return self

    def find_uinode(self):
        pass

    def walk_uinode(self):
        has_descendant = len(self.descendant) > 0
        yield {
            "selector": self.selector,
            "name": self.name,
            "has_descendant": has_descendant
        }
        for selector_or_construactor, name in self.descendant:
            if isinstance(selector_or_construactor, str):
                yield {
                    "selector": selector_or_construactor,
                    "name": name,
                    "has_descendant": False
                }
            else:
                definition = selector_or_construactor.definition
                nodes = definition.walk_uinode()


class UINode():

    def __init__(self, selector, name, has_descendants):
        self.selector = selector
        self.name = name
        self.has_descendants = has_descendants


class Descnedant():

    def __init__(self, selector, name):
        self.selector = selector
        self.name = name
