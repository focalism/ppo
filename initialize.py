
import os
from src.utils import get_config
from selenium import webdriver
from src.common import BrowserOptions
from src.context_factory import ContextFactory


yaml_path = os.path.join(os.getcwd(), 'test/browser.yaml')
if not os.path.exists(yaml_path):
    yaml_path = os.path.join(os.getcwd(), 'browser.yaml')
config = get_config(yaml_path)
browser_option = BrowserOptions(config['browser_options'])



def initialize(options: BrowserOptions):
    options_args = {}
    if options.browser_name == 'firefox':
        browser_options = webdriver.FirefoxOptions()
        browser = webdriver.Firefox()
        options_args.update({'firefox_options':browser_options})
    elif options.browser_name == 'safari':
        browser_options = None
        browser = webdriver.Safari
    elif options.browser_name == 'ie':
        browser_options = webdriver.IeOptions()
        browser = webdriver.Ie
        options_args.update({'ie_options':browser_options})
    elif options.browser_name == 'edge':
        browser_options = None
        browser = webdriver.Edge
    else:
        browser_options = webdriver.ChromeOptions()
        browser = webdriver.Chrome
        options_args.update({'chrome_options': browser_options})

    if browser_options:
        if options.headless:
            browser_options.add_argument('headless')
            browser_options.add_argument('no-sandbox')
            browser_options.add_argument('disable-gpu')
        else:
            browser_options.add_argument('window-size={},{}'.format(
                options.wind_size_x, options.wind_size_y))
    if options.executable_path:
        options_args.update({'executable_path':options.executable_path})
    browser = browser(**options_args)

    if not options.report_dir:
        options.report_dir = os.getcwd()
    if not os.path.exists(options.report_dir):
        os.makedirs(options.report_dir)
    factory = ContextFactory(browser)
    return factory.create()

context = initialize(browser_option)
