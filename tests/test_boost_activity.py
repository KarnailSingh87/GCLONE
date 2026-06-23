import re
from boost_activity import _generate_dates


def test_generate_dates_count_and_format():
    dates = _generate_dates(10, 30)
    assert len(dates) == 10
    iso_like = re.compile(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$")
    for d in dates:
        assert iso_like.match(d)


def test_generate_dates_sorted():
    dates = _generate_dates(50, 5)
    assert dates == sorted(dates)
