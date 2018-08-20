from .page import Page


class PageFactory:

    def __init__(self, context):
        self.context = context


    def create(self, page: Page):
        page.context = self.context
        return page

    def wait_for(self, page:Page):
        if page.url:
            self.context.browser.get(page.url)
        for panel in page.init_panels:
            self.context.wait_for(panel)
        return self.create(page)