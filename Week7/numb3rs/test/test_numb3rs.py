from numb3rs import validate

def test_valid():
    assert validate("255.255.255.255") == True

def test_boundary():
    assert validate("512.512.512.512") == False
    assert validate("256.12.124.42") == False


def test_digit():
    assert validate("1.2.3.1000") == False
    assert validate("1.2.3.4") == True

def test_onedigit():
    assert validate("124.0.0.1") == True

def test_text():
    assert validate("cat") == False