
from .context import Context


class ContextFactory:
    def __init__(self, browser):
        self.browser = browser
        pass

    def create(self):
        return Context(self.browser)
