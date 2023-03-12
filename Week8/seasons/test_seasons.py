from seasons import get_minutes
from datetime import date


def test_my():
    assert get_minutes(date(2005,10,29)) == "nine million, one hundred and thirty-two thousand, four hundred and eighty point zero, minutes"

