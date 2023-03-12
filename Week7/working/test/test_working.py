from working import convert 

def test_base1():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_base2():
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"

def test_min():
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"