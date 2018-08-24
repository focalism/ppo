from .page_factory import PageFactory
from .panel_factory import PanelFactory
from .common import BrowserOptions


class Context:

    def __init__(self, driver, options: BrowserOptions=None):
        self.action_chain = driver.common.action_chains.ActionChains
        if options.browser_name == 'firefox':
            browser_options = driver.FirefoxOptions()
            browser = driver.Firefox
        elif options.browser_name == 'safari':
            browser_options = None
            browser = driver.Safari
        elif options.browser_name == 'ie':
            browser_options = driver.IeOptions()
            browser = driver.Ie
        elif options.browser_name == 'edge':
            browser_options = None
            browser = driver.Edge
        else:
            browser_options = driver.ChromeOptions()
            browser = driver.Chrome

        if browser_options:
            if options.headless:
                browser_options.add_argument('headless')
                browser_options.add_argument('no-sandbox')
                browser_options.add_argument('disable-gpu')
            else:
                browser_options.add_argument('window-size={},{}'.format(
                    options.wind_size_x, options.wind_size_y))
        if options.executable_path:
            self.browser = browser(executable_path=options.executable_path)
        else:
            self.browser = browser()

    def wait_for(self, page_or_panel):
        if page_or_panel.kind == 'panel':
            factory = PanelFactory(self, page_or_panel)
        else:
            factory = PageFactory(self, page_or_panel)
        return factory.wait_for()

    def close(self):
        self.browser.close()

    def quit(self):
        self.browser.quit()



