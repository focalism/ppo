from panel.post_panel import PostPanel1
from page.post_page import PostPage
from initialize import context
from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get('http://192.168.30.115:8000/test.html')
# selector = browser.find_element_by_css_selector('body div:nth-child(2) li:nth-child(1)')
# print(selector.text)
# browser.close()


def test_page_wait_for():
    context.wait_for(PostPage)
    context.close()

test_page_wait_for()

# drive = webdriver.Chrome
# browser = drive()
# browser.close()

# drive.get('https://www.baidu.com')
# element = drive.find_element_by_id('s_tab')
# html = element.get_attribute('outerHTML')
# # attr = element.get_property('attributes')[0]
# drive.close()
# drive.quit()
# print(html)

#
# ui_definition = PostPanel1().definition
# for node in ui_definition.walk_ui_node():
#     print(node)