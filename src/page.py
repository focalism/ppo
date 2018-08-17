from .context import Context


class Page():

    def __init__(self, browser_name):
        self.context = Context(browser_name).browser
        self.init_panel = list()
        self.url = None
