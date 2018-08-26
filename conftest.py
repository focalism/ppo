from initialize import context
import pytest
from _pytest.runner import runtestprotocol


@pytest.fixture(scope='session')
def fixture_session():
    yield context
    context.close()


def pytest_runtest_protocol(item, next_item):
    reports = runtestprotocol(item, nextitem=next_item)
    for report in reports:
        if report.when == 'call':
            if report.outcome == 'failed':
                picture_name = item.name + '.png'
                context.browser.save_screenshot(picture_name)
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
