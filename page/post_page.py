from src.page import Page
from panel.post_panel import PostPanel1
from panel.post_panel import PostPanel2


class PostPage(Page):
    init_panels =  [PostPanel1, PostPanel2]
    url = 'http://192.168.30.115:8000/test.html'
    kind = 'page'

