from .uidefinition import UIDefinition
from selenium.webdriver.remote.webdriver import WebElement
from .context import Context


class Panel:
    kind = 'panel'
    definition: UIDefinition = UIDefinition
    context: Context = None
    element: WebElement = None

    def __init__(self):
        pass

    @classmethod
    def find_ui_node(cls, name):
        for node in cls.definition.walk_ui_node():
            if name == node["name"]:
                return node

    def click(self, name):
        element = self.get_element_by_name(name)
        element.click()
        windows = self.context.browser.window_handles()
        self.context.browser.switch_to_window(windows[len(windows)-1])

    def right_click(self, name):
        element = self.get_element_by_name(name)
        self.context.action_chain(self.context.browser).context_click(element).perform()

    def double_click(self, name):
        element = self.get_element_by_name(name)
        self.context.action_chain(self.context.browser).double_click(element).perform()

    def press(self, name):
        element = self.get_element_by_name(name)
        pass

    def clear(self, name):
        element = self.get_element_by_name(name)
        element.clear()

    def type(self, name, text):
        element = self.get_element_by_name(name)
        element.send_keys(text)

    def hover(self, name):
        element = self.get_element_by_name(name)
        self.context.action_chain(self.context.browser).move_to_element(element).perform()

    def text_of(self, name):
        element = self.get_element_by_name(name)
        return element.text

    def html_of(self, name):
        element = self.get_element_by_name(name)
        pass

    def get_element_by_name(self, name):
        if name == self.definition.name:
            return self.element
        else:
            node = self.find_ui_node(name)
            element = self.element.find_element_by_css_selector(node['selector'])
            return element

    def get_attribute(self, name):
        element = self.get_element_by_name(name)
        return element.get_attributes()

    def select_all(self):
        pass

    def select_unique(self):
        pass

    def select_first(self):
        pass

    def wait_for(self):
        for node in self.definition.walk_ui_node():
            self.context.browser.find_element_by_css_selector(node['selector'])