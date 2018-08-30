from initialize import context
from initialize import browser_option
import pytest
from os.path import join
from _pytest.runner import runtestprotocol


@pytest.fixture(scope='function')
def fixture_function():
    return context

@pytest.fixture(scope='session')
def fixture_teardown():
    context.quit()


def pytest_runtest_setup(item):
    context.browser.execute_script("window.open('');")
    context.browser.switch_to.window(context.browser.window_handles[-1])



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


def pytest_runtest_teardown(item):
    context.browser.close()
    context.browser.switch_to.window(context.browser.window_handles[-1])