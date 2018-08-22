from selenium import webdriver
from .page_factory import PageFactory
from .panel_factory import PanelFactory
from selenium.webdriver.common.action_chains import ActionChains


class Context:

    def __init__(self, browser_name=None):
        self.action_chain = ActionChains
        if browser_name == 'firefox':
            self.browser = webdriver.Firefox()
        elif browser_name == 'safari':
            self.browser = webdriver.Safari().window_handles()
        elif browser_name == 'ie':
            self.browser = webdriver.Ie()
        elif browser_name == 'edge':
            self.browser = webdriver.Edge()
        else:
            self.browser = webdriver.Chrome()

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


class BrowserOptions:

    def __init__(self, headless=False, screenshot=False, report_dir=None):
        self.headless = headless
        self.screenshot = screenshot

