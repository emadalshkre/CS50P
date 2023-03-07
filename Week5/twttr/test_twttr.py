from twttr import shorten

def test_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("") == ""
    assert shorten("2348") == "2348"