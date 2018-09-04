from panel.post_panel import PostPanel1
from panel.click_test_panel import ClickPanel
from panel.click_test_panel import LoginPanel
from panel.click_test_panel import MouseOverPanel
from selenium.webdriver.remote.webdriver import WebElement
from src.context import Context


def test_find_ui_node(fixture_session: Context):
    fixture_session.browser.get('file:///D:/code/ppo/test.html')
    panel = fixture_session.wait_for(PostPanel1)
    node = panel.find_ui_node('post1')
    assert (node['selector'] == 'body div:nth-child(1)')
    assert (node['name'] == 'post1')


def test_click_element(fixture_session: Context):
    fixture_session.browser.get('file:///D:/code/ppo/test/html/click_test.html')
    panel = fixture_session.wait_for(ClickPanel)
    assert (panel.text_of('single') == 'Single-click me')
    panel.click('single')
    assert (panel.text_of('single') == 'I was Single-clicked!')


def test_double_click_element(fixture_session: Context):
    fixture_session.browser.get('file:///D:/code/ppo/test/html/click_test.html')
    panel = fixture_session.wait_for(ClickPanel)
    assert (panel.text_of('double') == 'Double-click me')
    panel.double_click('double')
    assert (panel.text_of('double') == 'I was double-clicked!')


def test_page_jump(fixture_session: Context):
    fixture_session.browser.get('file:///D:/code/ppo/test/html/click_test.html')
    panel = fixture_session.wait_for(ClickPanel)
    panel.click('jump')
    assert (panel.context.browser.current_url == 'file:///D:/code/ppo/test.html')


def test_page_jump_new(fixture_session: Context):
    fixture_session.browser.get('file:///D:/code/ppo/test/html/click_test.html')
    panel = fixture_session.wait_for(ClickPanel)
    panel.click('jump new')
    assert (panel.context.browser.current_url == 'file:///D:/code/ppo/test.html')


def test_clear_default_value(fixture_session: Context):
    fixture_session.browser.get('file:///D:/code/ppo/test/html/click_test.html')
    panel = fixture_session.wait_for(LoginPanel)
    assert (panel.get_attribute('name', 'value') == 'John')
    panel.clear('name')
    assert (panel.get_attribute('name', 'value') == '')


def test_type_value(fixture_session: Context):
    fixture_session.browser.get('file:///D:/code/ppo/test/html/click_test.html')
    panel = fixture_session.wait_for(LoginPanel)
    assert (panel.get_attribute('name', 'value') == 'John')
    panel.clear('name')
    panel.type('name', 'xuzg')
    assert (panel.get_attribute('name', 'value') == 'xuzg')


def test_mouse_over(fixture_session: Context):
    fixture_session.browser.get('file:///D:/code/ppo/test/html/click_test.html')
    panel = fixture_session.wait_for(MouseOverPanel)
    panel.hover('hover')
    assert (panel.text_of('hover') == 'I was Mouse-over!')


def test_text_of(fixture_session: Context):
    fixture_session.browser.get('file:///D:/code/ppo/test/html/click_test.html')
    panel = fixture_session.wait_for(ClickPanel)
    text = panel.text_of('double')
    assert (text == 'Double-click me')


def test_inner_html(fixture_session: Context):
    fixture_session.browser.get('file:///D:/code/ppo/test/html/click_test.html')
    panel = fixture_session.wait_for(ClickPanel)
    inner_html = panel.inner_html('jump')
    assert ('id="jump"' not in inner_html)
    assert ('a href=' in inner_html)


def test_outer_html(fixture_session: Context):
    fixture_session.browser.get('file:///D:/code/ppo/test/html/click_test.html')
    panel = fixture_session.wait_for(ClickPanel)
    outer_html = panel.outer_html('jump')
    assert ('id="jump"' in outer_html)
    assert ('a href=' in outer_html)


def test_get_element_by_name(fixture_session: Context):
    fixture_session.browser.get('file:///D:/code/ppo/test/html/click_test.html')
    panel = fixture_session.wait_for(ClickPanel)
    element = panel.get_element_by_name('jump')
    assert (isinstance(element, WebElement))


def test_get_attribute(fixture_session: Context):
    fixture_session.browser.get('file:///D:/code/ppo/test/html/click_test.html')
    panel = fixture_session.wait_for(LoginPanel)
    assert (panel.get_attribute('name', 'value') == 'John')


def test_get_attributes(fixture_session: Context):
    fixture_session.browser.get('file:///D:/code/ppo/test/html/click_test.html')
    panel = fixture_session.wait_for(ClickPanel)
    attrs = panel.get_attributes('single')
    assert (attrs['id'] == 'single_click')
    assert (attrs['onclick'] == 'SingleClick()')


def test_wait_for_element_locate_with_name(fixture_session: Context):
    fixture_session.browser.get('file:///D:/code/ppo/test/html/click_test.html')
    panel = fixture_session.wait_for(ClickPanel)
    panel.wait_for_all_element_locate(name='single')


def test_wait_for_element_locate_with_css_selector(fixture_session: Context):
    fixture_session.browser.get('file:///D:/code/ppo/test/html/click_test.html')
    panel = fixture_session.wait_for(ClickPanel)
    panel.wait_for_all_element_locate(css_selector='#single_click')
