
import os
from src.utils import get_config
from selenium import webdriver
from src.common import BrowserOptions
from src.context_factory import ContextFactory


yaml_path = os.path.join(os.getcwd(), 'test/browser.yaml')
if not os.path.exists(yaml_path):
    yaml_path = os.path.join(os.getcwd(), 'test/browser.yaml')
config = get_config(yaml_path)


def initialize(options: BrowserOptions):
    if options.browser_name == 'firefox':
        browser_options = webdriver.FirefoxOptions()
        browser = webdriver.Firefox
    elif options.browser_name == 'safari':
        browser_options = None
        browser = webdriver.Safari
    elif options.browser_name == 'ie':
        browser_options = webdriver.IeOptions()
        browser = webdriver.Ie
    elif options.browser_name == 'edge':
        browser_options = None
        browser = webdriver.Edge
    else:
        browser_options = webdriver.ChromeOptions()
        browser = webdriver.Chrome

    if browser_options:
        if options.headless:
            browser_options.add_argument('headless')
            browser_options.add_argument('no-sandbox')
            browser_options.add_argument('disable-gpu')
        else:
            browser_options.add_argument('window-size={},{}'.format(
                options.wind_size_x, options.wind_size_y))
    if options.executable_path:
        browser = browser(executable_path=options.executable_path)
    else:
        browser = browser()

    if not options.report_dir:
        options.report_dir = os.getcwd()
    if not os.path.exists(options.report_dir):
        os.makedirs(options.report_dir)
    factory = ContextFactory(browser)
    context = factory.create()
    return context

context = initialize(config)