from .page import Page


class PageFactory:

    def __init__(self, context, page: Page):
        self.context = context
        self.page = page

    def create(self):
        return self.page(self.context)

    def wait_for(self, page: Page):
        if page.url:
            self.context.browser.get(page.url)
        for panel in page.init_panels:
            self.context.wait_for(panel)
        return self.create()
