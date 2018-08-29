class BrowserOptions:
    def __init__(self,configs):
        self.browser_name = configs['browser_name']
        self.headless = configs['headless']
        self.screen_shot = configs['screen_shot']
        self.report_dir = configs['report_dir']
        self.wind_size_x = configs['wind_size_x']
        self.wind_size_y = configs['wind_size_y']
        self.executable_path = configs['executable_path']

class Browser:
    def __init__(self, browser, excutor_path, options):
        self.executor_path = excutor_path
        self.options = options
        self.browser = browser

