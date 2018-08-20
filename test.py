from panel.post_panel import PostPanel1
from page.post_page import PostPage
from src.context import Context

# browser = webdriver.Chrome()
# browser.get('http://192.168.30.115:8000/test.html')
# selector = browser.find_element_by_css_selector('body div:nth-child(2) li:nth-child(1)')
# print(selector.text)
# browser.close()

def test_page_wait_for():
    context = Context()
    context.wait_for(PostPage)
    context.close()

test_page_wait_for()
