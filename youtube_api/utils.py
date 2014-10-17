def minutes_and_seconds_from_duration(duration):
    """
    Returns a tuple of integers minutes, seconds
    :param duration:
    :return:
    """
    minutes, seconds = duration[2:].split('M')
    return int(minutes), int(seconds[:-1])


def duration_in_seconds(duration):
    minutes, seconds = minutes_and_seconds_from_duration(duration)
    return minutes*60 + seconds
