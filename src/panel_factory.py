from .panle import Panel

class PanelFactory:
    def __init__(self, context):
        self.context = context
        self.element = None

    def create(self, panel: Panel):
        panel.context = self.context
        panel.element = self.element
        return panel

    def wait_for(self, panel: Panel):
        selector = panel.definition.selector
        self.element = self.context.browser.find_element_by_css_selector(selector)
        for node in panel.definition.walk_ui_node():
            self.context.browser.find_element_by_css_selector(node['selector'])
        return self.create(panel)