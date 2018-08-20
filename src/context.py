from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from .page_factory import PageFactory
from .panel_factory import PanelFactory


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


    def wait_for(self,page_or_panel):
        if page_or_panel.kind == 'panel':
            factory = PanelFactory(self)
        else:
            factory = PageFactory(self)
        return factory.wait_for(page_or_panel)

    def close(self):
        self.browser.close()

    def quit(self):
        self.browser.quit()


class BrowserOptions:

    def __init__(self, headless=False, screenshot=False, report_dir=None):
        self.headless = headless
        self.screenshot = screenshot

