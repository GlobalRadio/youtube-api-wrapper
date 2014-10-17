===========
Basic usage
===========

Videos
------

The VideoApi class gives access to the `Videos API endpoint. <https://developers.google.com/youtube/v3/docs/videos>`_ .

.. automodule:: VideoApi
   :members:

Examples:

.. code-block:: python

    from youtube_api.client import VideoApi

    client = VideoApi('API_KEY')

    video = client.get_video_by_id('Video Id')


By default only snippet part is retrieved. `Querying for more parts. <https://developers.google.com/youtube/v3/getting-started#part>`_
results in an higher quota consumption. It's possible to check the quota used before submitting the query by calling:

.. code-block:: python

    client.calculate_quota(('snippet', 'contentDetails'))
    >>> 4