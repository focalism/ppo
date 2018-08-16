from selenium import webdriver


class Context():

    def __init__(self, browser_name):
        if browser_name == 'firefox':
            self.browser = webdriver.Firefox()
        if browser_name == 'chrome':
            self.browser = webdriver.Chrome()
        if browser_name == 'ie':
            self.browser = webdriver.Ie()
        if browser_name == 'edge':
            self.browser = webdriver.Edge()
        if browser_name == 'safari':
            self.browser == webdriver.Safari()
