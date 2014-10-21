import re

DURATION_REGEX = re.compile(r'PT(?P<minutes>\d+)M(?P<seconds>\d+)')

def minutes_and_seconds_from_duration(duration):
    """
    Returns a tuple of integers minutes, seconds from the YouTube duration format
    which is PT3M20S
    :param duration: string YouTube duration
    :return:
    """
    match = DURATION_REGEX.match(duration)
    minutes = match.group('minutes')
    seconds = match.group('seconds')
    return int(minutes), int(seconds)


def duration_in_seconds(duration):
    minutes, seconds = minutes_and_seconds_from_duration(duration)
    return minutes*60 + seconds
