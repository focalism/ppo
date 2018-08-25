from .page_factory import PageFactory
from .panel_factory import PanelFactory


class Context:

    def __init__(self, browser):
        self.browser = browser

    def wait_for(self, page_or_panel):
        if page_or_panel.kind == 'panel':
            factory = PanelFactory(self, page_or_panel)
        else:
            factory = PageFactory(self, page_or_panel)
        return factory.wait_for()

    def close(self):
        self.browser.close()

    def quit(self):
        self.browser.quit()



