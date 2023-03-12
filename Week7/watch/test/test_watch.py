from watch import parse

def test_http():
    assert parse("http://youtube.com/embed/xvFZjo5PgG0") == "https://youtu.be/xvFZjo5PgG0"
    assert parse("https://youtube.com/embed/xvFZjo5PgG0") == "https://youtu.be/xvFZjo5PgG0"

def test_www():
    assert parse("https://www.youtube.com/embed/xvFZjo5PgG0") == "https://youtu.be/xvFZjo5PgG0"
