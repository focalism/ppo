from panel.post_panel import PostPanel1
from src.context import Context

def test_click_element(fixture_function: Context):
    fixture_function.browser.get('http://192.168.30.115:8000/test.html')
    panel = fixture_function.wait_for(PostPanel1)
    node = panel.find_ui_node('title')
    assert (node['selector'] == 'body div:nth-child(1) h2')
    assert (node['name'] == 'title')
    panel.click('link')



def test_find_ui_node(fixture_function: Context):
    fixture_function.browser.get('http://192.168.30.115:8000/test.html')
    panel = fixture_function.wait_for(PostPanel1)
    node = panel.find_ui_node('post1')
    assert (node['selector'] == 'body div:nth-child(1)')
    assert (node['name'] == 'post1')



