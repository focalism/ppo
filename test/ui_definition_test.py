from panel.todo_panle import TodoApp
from src.panel import Panel

ui_definition = TodoApp.definition


def test_root():
    assert (ui_definition.name == 'app')
    assert (ui_definition.selector == 'div.app')


def test_with_descendant_selector():
    assert (ui_definition.descendant[0][0] == 'div.sa')
    assert (ui_definition.descendant[0][1] == 'title')


def test_with_descendant_with_panel():
    assert (len(ui_definition.descendant) == 4)
    assert (isinstance(ui_definition.descendant[3][0](), Panel))


def test_walk_ui_node():
    node_list = []
    for node in ui_definition.walk_ui_node():
        node_list.append(node)
    assert (len(node_list) == 12)
    assert (node_list[0]['selector'] == 'div.app')
    assert (node_list[0]['name'] == 'app')
    assert (node_list[0]['has_descendant'] is True)
    assert (node_list[1]['selector'] == 'div.app div.sa')
    assert (node_list[1]['name'] == 'title')
    assert (node_list[1]['has_descendant'] is False)
    assert (node_list[4]['selector'] == 'div.app test')
    assert (node_list[4]['name'] != 'test')
    assert (node_list[4]['name'] == 'post_panel2')
    assert (node_list[4]['has_descendant'] is True)
    assert (node_list[8]['selector'] == 'div.app test div.add')
    assert (node_list[8]['name'] == 'and')
    assert (node_list[8]['has_descendant'] is True)


def test_find_ui_node():
    node = ui_definition.find_ui_node('title')
    assert (node['name'] == 'title')
    assert (node['selector'] == 'div.app div.sa')
    assert (node['has_descendant'] is False)
    node = ui_definition.find_ui_node('test')
    assert (node is None)
    node = ui_definition.find_ui_node('post_panel2')
    assert (node['selector'] == 'div.app test')


