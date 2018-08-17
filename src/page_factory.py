from .page import Page
from .context import Context


class PageFactory():

    def __init__(self, browser_name):
        self.browser_name = browser_name
        self.context = Context(browser_name)

    def create(self):
        return Page(self.browser_name)

    def wait_for(self, page_constructor):
        browser = self.context.browser
        if page_constructor.url:
            browser.goto(page_constructor.url)
        for panel in page_constructor.init_panel:
            self.context.wait_for(panel)
        return self.create()
