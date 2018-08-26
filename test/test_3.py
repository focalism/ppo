from page.post_page import PostPage


def test_page_wait_for(fixture_session):
    fixture_session.wait_for(PostPage)
    assert False



def test_page_wait_for_2(fixture_session):
    fixture_session.wait_for(PostPage)
    assert False
