from fuel import convert, gauge


def test_type():
    assert convert("1/3") == 1/3 * 100
    assert convert("4/4") == 100
    assert convert("2/1") == 200


def test_gauge():
    assert gauge(25) == "25"
    assert gauge(100) == "F"
    assert gauge(1) == "E"