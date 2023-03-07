from plates import is_valid

def test_len():
    assert is_valid("H") == False
    assert is_valid("OUTATIME") == False


def test_punctuation():
    assert is_valid("PI3.14") == False

def test_number():
    assert is_valid("CS05") == False
    assert is_valid("PI3.14") == False

def test_default():
    assert is_valid("CS50") == True