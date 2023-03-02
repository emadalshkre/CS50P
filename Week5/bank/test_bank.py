from bank import value

def test_value():
    assert value("HELLO") == 0
    assert value("he3248") == 20
    assert value("37") == 100