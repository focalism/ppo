from .context import Context
from .panle import Panel


class PanelFactory():
    def __init__(self, browser_name):
        self.browser_name = browser_name
        self.context = Context(self.browser_name)
        self.browser = self.context.browser

    def create(self, element_handle):
        return Panel(self.browser_name)

    def wait_for(self, panel_constructor):
        uidefinition = panel_constructor.definition
        selector = uidefinition.selector
