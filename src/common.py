class BrowserOptions:

    def __init__(self,
                 browser_name=None,
                 headless=False,
                 screen_shot=False,
                 report_dir=None,
                 wind_size_x=0,
                 wind_size_y=0,
                 executable_path=None):
        self.browser_name = browser_name
        self.headless = headless
        self.screen_shot = screen_shot
        self.report_dir = report_dir
        self.wind_size_x = wind_size_x
        self.wind_size_y = wind_size_y
        self.executable_path = executable_path
