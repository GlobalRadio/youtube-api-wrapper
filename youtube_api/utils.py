import re
from datetime import datetime



YT_CREATION_TIMESTAMP = 1108339200

DURATION_REGEX = re.compile(r'PT(?P<minutes>\d+)M(?P<seconds>\d+)')

def minutes_and_seconds_from_duration(duration):
    """
    Returns a tuple of integers minutes, seconds from the YouTube duration format
    which is PT3M20S
    :param duration: string YouTube duration
    :return: tuple of integers
    """
    match = DURATION_REGEX.match(duration)
    minutes = match.group('minutes')
    seconds = match.group('seconds')
    return int(minutes), int(seconds)


def duration_in_seconds(duration):
    minutes, seconds = minutes_and_seconds_from_duration(duration)
    return minutes*60 + seconds

def get_utc_from_timestamp(timestamp):
    try:
        timestamp = int(timestamp)
    except:
        timestamp = YT_CREATION_TIMESTAMP
    if timestamp == 0: timestamp = YT_CREATION_TIMESTAMP
    return datetime.utcfromtimestamp(timestamp)

def get_utc_from_string(timestamp):
    if not timestamp:
        return datetime.utcfromtimestamp(YT_CREATION_TIMESTAMP)
    try:
        timestamp = datetime.strptime(str(timestamp),  "%Y-%m-%dT%H:%M:%S.%fZ")
        return timestamp
    except:
        return datetime.utcfromtimestamp(YT_CREATION_TIMESTAMP)
