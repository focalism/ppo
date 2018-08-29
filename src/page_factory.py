from .page import Page


class PageFactory:

    def __init__(self, context, page: Page):
        self.context = context
        self.page = page

    def create(self):
        self.page.context = self.context
        return self.page()

    def wait_for(self,timeout=10):
        if self.page.url:
            self.context.browser.implicity_wait(timeout)
            self.context.browser.get(self.page.url)
        for panel in self.page.init_panels:
            self.context.wait_for(panel)
        return self.create()
