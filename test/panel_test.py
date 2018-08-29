from panel.post_panel import PostPanel1
from src.context import Context

def test_find_ui_node(fixture_session: Context):
    fixture_session.browser.get('http://192.168.30.115:8000/test.html')
    panel = fixture_session.wait_for(PostPanel1)
    node = panel.find_ui_node('post1')
    assert (node['selector'] == 'body div:nth-child(1)')
    assert (node['name'] == 'post1')

def test_click_element(fixture_session: Context):
    panel = fixture_session.wait_for(PostPanel1)
    node = panel.find_ui_node('title')
    assert (node['selector'] == 'body div:nth-child(1) h2')
    assert (node['name'] == 'title')
    panel.click('link')