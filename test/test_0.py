class TestFixtureScope(object):
    def test_one(self, fixture_session, fixture_module, fixture_class, fixture_function):
        assert fixture_session == 'fixture_session'
        assert fixture_module == 'fixture_module'
        assert fixture_class == 'fixture_class'
        assert fixture_function == 'fixture_function'
        # assert False

    def test_two(self, fixture_session, fixture_module, fixture_class, fixture_function):
        assert fixture_session == 'fixture_session'
        assert fixture_module == 'fixture_module'
        assert fixture_class == 'fixture_class'
        assert fixture_function == 'fixture_function'
        # assert False


def test_three(fixture_session, fixture_module, fixture_class, fixture_function):
    assert fixture_session == 'fixture_session'
    assert fixture_module == 'fixture_module'
    assert fixture_class == 'fixture_class'
    assert fixture_function == 'fixture_function'
    assert False