from initialize import context
from initialize import browser_option
import pytest
from os.path import join


@pytest.fixture(scope='session')
def fixture_session():
    yield context
    context.quit()


@pytest.fixture(scope='session')
def fixture_teardown():
    context.quit()


def pytest_runtest_setup():
    context.browser.execute_script("window.open('');")
    context.browser.switch_to.window(context.browser.window_handles[-1])


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    if rep.when == 'call':
        if rep.failed:
            if browser_option.screen_shot:
                report_dir = browser_option.report_dir
                picture_name = item.name + '.png'
                picture_path = join(report_dir, picture_name)
                context.browser.save_screenshot(picture_path)


def pytest_runtest_teardown():
    context.browser.close()
    context.browser.switch_to.window(context.browser.window_handles[-1])