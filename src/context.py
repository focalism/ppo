from selenium import webdriver
from .page_factory import PageFactory
from .panel_factor import PanelFactory


class Context():

    def __init__(self, browser_name):
        if browser_name == 'firefox':
            self.browser = webdriver.Firefox()
        if browser_name == 'chrome':
            self.browser = webdriver.Chrome()
        if browser_name == 'ie':
            self.browser = webdriver.Ie()
        if browser_name == 'edge':
            self.browser = webdriver.Edge()
        if browser_name == 'safari':
            self.browser == webdriver.Safari()

    def wait_for(self, constructor):
        if constructor.kind == 'panel':
            factory = PanelFactory()
        else:
            factory = PageFactory()

        return factory.wait_for(constructor)
