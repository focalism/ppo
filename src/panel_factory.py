from selenium.webdriver.remote.webdriver import WebElement


class PanelFactory:
    def __init__(self, context, panel, scope=None):
        self.context = context
        self.panel = panel
        self.scope = scope

    def create(self, element: WebElement):
        self.panel.context = self.context
        self.panel.element = element
        return self.panel()

    def wait_for(self):
        selector = self.panel.definition.selector
        if self.scope:
            element = self.scope.element.find_element_by_css_selector(selector)
        else:
            element = self.context.browser.find_element_by_css_selector(selector)
        for node in self.panel.definition.walk_ui_node():
            self.context.browser.find_element_by_css_selector(node['selector'])
        return self.create(element)

    def select_all(self):
        pass

    def select_first(self):
        pass

    def select_unique(self):
        pass
