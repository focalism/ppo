from panel.post_panel import PostPanel1
from src.panle import Panel

ui_definition = PostPanel1.definition


def test_root():
    assert (ui_definition.name == 'post1')
    assert (ui_definition.selector == 'body div:nth-child(1)')


def test_with_descendant_selector():
    assert (ui_definition.descendant[0][0] == 'h2')
    assert (ui_definition.descendant[0][1] == 'title')


def test_with_descendant_with_panel():
    assert (len(ui_definition.descendant) == 6)
    assert (isinstance(ui_definition.descendant[5][0](), Panel))


def tet_walk_ui_node():
    node_list = []
    for node in ui_definition.walk_ui_node():
        node_list.append(node)
    assert (len(node_list) == 12)
    assert (node_list[0]['selector'] == 'body div:nth-child(1)')
    assert (node_list[0]['name'] == 'post1')
    assert (node_list[0]['has_descendant'] is True)
    assert (node_list[1]['selector'] == 'body div:nth-child(1) h2')
    assert (node_list[1]['name'] == 'title')
    assert (node_list[1]['has_descendant'] is False)
    assert (node_list[6]['selector'] == 'body div:nth-child(1) body div:nth-child(2)')
    assert (node_list[6]['name'] == 'post2')
    assert (node_list[6]['has_descendant'] is True)
    assert (node_list[7]['selector'] == 'body div:nth-child(1) body div:nth-child(2) h2')
    assert (node_list[7]['name'], 'title')
    assert (node_list[7]['has_descendant'] is False)


def test_find_ui_node():
    node = ui_definition.find_ui_node('title')
    assert (node['name'] == 'title')
    assert (node['selector'] == 'body div:nth-child(1) h2')
    assert (node['has_descendant'] is False)
    node = ui_definition.find_ui_node('test')
    assert (node is None)
    node = ui_definition.find_ui_node('post_panel2')
    assert (isinstance(node['selector'])







