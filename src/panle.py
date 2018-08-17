from .context import Context


class Panel():

    def __init__(self, browser_name):
        self.context = Context(browser_name).browser
        self.kind = "panel"
        self.definition = None

    @property
    def element_handle(self):
        self.context.find_element_by_css_selector(self.definition.selector)

    def find_uinode(self):
        pass

    def walk_uinode(self):
        pass

    def click(self):
        pass

    def press(self):
        pass

    def type(self):
        pass

    def hover(self):
        pass

    def text_of(self):
        pass

    def html_of(self):
        pass

    def get_element_by_name(self, name):
        if name == self.definition.name:
            return self.element_handle
        else:
            pass

    def select_all(self):
        pass

    def select_unique(self):
        pass

    def select_first(self):
        pass

    def waitfor(self):
        pass
