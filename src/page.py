
class Page:
    init_panels = list()
    url = None
    context = None

    def __init__(self):
        pass

    def wait_for(self):
        for panel in self.init_panels:
            panel.wait_for()
