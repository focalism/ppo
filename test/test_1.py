def test_four(fixture_session, fixture_module, fixture_class, fixture_function, foo):
    assert fixture_session == 'fixture_session'
    assert fixture_module == 'fixture_module'
    assert fixture_class == 'fixture_class'
    assert fixture_function == 'fixture_function'
    assert False