from panel.post_panel import PostPanel1
from panel.click_test_panel import ClickPanel
from panel.click_test_panel import LoginPanel
from panel.click_test_panel import MouseOverPanel
from src.context import Context


def test_find_ui_node(fixture_session: Context):
    fixture_session.browser.get('http://192.168.30.115:8000/test.html')
    panel = fixture_session.wait_for(PostPanel1)
    node = panel.find_ui_node('post1')
    assert (node['selector'] == 'body div:nth-child(1)')
    assert (node['name'] == 'post1')


def test_click_element(fixture_session: Context):
    fixture_session.browser.get('file:///D:/code/ppo/test/html/click_test.html')
    panel = fixture_session.wait_for(ClickPanel)
    assert  (panel.text_of('single')== 'Single-click me')
    panel.click('single')
    assert (panel.text_of('single') == 'I was Single-clicked!')

def test_double_click_element(fixture_session: Context):
    fixture_session.browser.get('file:///D:/code/ppo/test/html/click_test.html')
    panel = fixture_session.wait_for(ClickPanel)
    assert  (panel.text_of('double')== 'Double-click me')
    panel.double_click('double')
    assert (panel.text_of('double') == 'I was double-clicked!')


def test_page_jump(fixture_session:Context):
    fixture_session.browser.get('file:///D:/code/ppo/test/html/click_test.html')
    panel = fixture_session.wait_for(ClickPanel)
    panel.click('jump')
    assert (panel.context.browser.current_url == 'file:///D:/code/ppo/test.html')

def test_page_jump_new(fixture_session:Context):
    fixture_session.browser.get('file:///D:/code/ppo/test/html/click_test.html')
    panel = fixture_session.wait_for(ClickPanel)
    panel.click('jump new')
    assert (panel.context.browser.current_url == 'file:///D:/code/ppo/test.html')

def test_clear_default_value(fixture_session:Context):
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


