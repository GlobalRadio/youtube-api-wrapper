def humanize_youtube_duration(duration):
    """
    https://developers.google.com/youtube/v3/docs/videos

    :param duration: string in the YouTube format
    :return: string with formatted duration
    """
    minutes, seconds = duration[2:].split('M')
    return '{minutes} min {seconds} sec'.format(minutes=minutes, seconds=seconds[:-1])