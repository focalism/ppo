from initialize import context
from initialize import browser_option
import pytest
import time
from os.path import join
from _pytest.runner import runtestprotocol


@pytest.fixture(scope='session')
def fixture_session():
    yield context


def pytest_runtest_protocol(item):
    reports = runtestprotocol(item)
    for report in reports:
        if report.when == 'call':
            if report.outcome == 'failed':
                if browser_option.screen_shot:
                    report_dir = browser_option.report_dir
                    picture_name = item.name + '.png'
                    picture_path = join(report_dir, picture_name)
                    context.browser.save_screenshot(picture_path)
    return True


@pytest.fixture(scope='module')
def fixture_module():
    pass


@pytest.fixture(scope='class')
def fixture_class():
    pass


@pytest.fixture(scope='function')
def fixture_function():
    pass
