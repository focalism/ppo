import os
from .common import BrowserOptions
from .context_factory import ContextFactory


def initialize(options: BrowserOptions):
    if not options.report_dir:
        options.report_dir = os.getcwd()

    if not os.path.exists(options.report_dir):
        os.makedirs(options.report_dir)

    factory = ContextFactory()


