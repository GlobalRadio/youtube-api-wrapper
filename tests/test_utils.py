from youtube_api.utils import minutes_and_seconds_from_duration, duration_in_seconds

DURATION = 'PT3M20S'

def test_minutes_and_seconds_from_duration():
    assert minutes_and_seconds_from_duration(DURATION) == (3, 20)


def test_duration_in_seconds():
    assert duration_in_seconds(DURATION) == 200
