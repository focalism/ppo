from .uidefinition import UIDefinition
from .panel_factory import PanelFactory
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.common.action_chains import ActionChains


class Panel:
    kind = 'panel'
    definition: UIDefinition = UIDefinition
    context = None
    element: WebElement = None

    def __init__(self):
        self.WebDriverWait = WebDriverWait
        self.By = By
        self.EC = EC
        self.ActionChains = ActionChains


    def find_ui_node(self, name):
        for node in self.definition.walk_ui_node():
            if name == node["name"]:
                return node

    def click(self, name):
        element = self.get_element_by_name(name)
        element.click()
        windows = self.context.browser.window_handles
        self.context.browser.switch_to_window(windows[len(windows)-1])

    def right_click(self, name):
        element = self.get_element_by_name(name)
        self.ActionChains(self.context.browser).context_click(element).perform()

    def double_click(self, name):
        element = self.get_element_by_name(name)
        self.ActionChains(self.context.browser).double_click(element).perform()

    def clear(self, name):
        element = self.get_element_by_name(name)
        element.clear()

    def type(self, name, text):
        element = self.get_element_by_name(name)
        element.send_keys(text)

    def hover(self, name):
        element = self.get_element_by_name(name)
        self.ActionChains(self.context.browser).move_to_element(element).perform()

    def text_of(self, name):
        element = self.get_element_by_name(name)
        return element.text

    def inner_html(self, name):
        element = self.get_element_by_name(name)
        return element.get_attribute('innerHTML')

    def outer_html(self, name):
        element = self.get_element_by_name(name)
        return element.get_attribute('outerHTML')

    def get_element_by_name(self, name):
        if name == self.definition.name:
            return self.element
        else:
            node = self.find_ui_node(name)
            element = self.element.find_element_by_css_selector(node['selector'])
            return element

    def get_attribute(self, name, attr_name):
        element = self.get_element_by_name(name)
        return element.get_attribute(attr_name)

    def get_attributes(self, name):
        element = self.get_element_by_name(name)
        attributes = self.context.browser.execute_script(
            'var items = {}; '
            'for (index = 0; '
            'index < arguments[0].attributes.length; ++index)'
            ' { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; '
            'return items;', element)
        return attributes

    def wait_for_element_locate(self, name=None, css_selector=None, timeout=10):
        """ An expectation for checking that an element is present on the DOM
        of a page. This does not necessarily mean that the element is visible.
        locator - used to find the element
        returns the WebElement once it is located
        """
        if name:
            css_selector = self.find_ui_node(name)['selector']
        self.WebDriverWait(self.context.browser, timeout).until(
            self.EC.presence_of_element_located((self.By.CSS_SELECTOR, css_selector))
        )

    def wait_for_all_element_locate(self, name=None, css_selector=None, timeout=10):
        if name:
            css_selector = self.find_ui_node(name)['selector']
            self.WebDriverWait(self.context.browser, timeout).until(
                self.EC.presence_of_all_elements_located(self.By.CSS_SELECTOR, css_selector)
            )



    def select_all(self):
        pass

    def select_unique(self):
        pass

    def select_first(self):
        pass

    def wait_for(self, panel):
        factory = PanelFactory(self.context, panel)
        factory.wait_for()
