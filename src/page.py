
class Page:
    init_panels = list()
    url = None

    def __init__(self, context):
        self.context = context

    def wait_for(self):
        for panel in self.init_panels:
            panel.wait_for()
