import logging

import requests
from .exceptions import YouTubeBadRequest, YouTubeForbidden, PartNotAllowed, FilterNotAllowed, OneFilterAllowed, \
    OptionalParamNotAllowed


ENDPOINT = "https://www.googleapis.com/youtube/v3/{resource_type}"

logger = logging.getLogger(__name__)

class Client(object):
    """
    Generic class with common methods, not to be called directly
    """
    def __init__(self, api_key):
        self.api_key = api_key
        self.resource_type = None
        self.allowed_parts = None
        self.allowed_filters = None
        self.allowed_optional_params = None

    def get_resource(self, resource_filter, parts, optional_params):
        """
        Low level generic method to get resource, used by other methods that add specific params for each resource

        :param resource_type: string with resource type to create the complete endpoint
        :param resource_filter: dictionary with the filter to be used
        :param parts: dictionary with the parts to be returned
        :param optional_params: dictionary with all the params
        :return: requests response object
        """
        ERRORS_MAPPING = {'400': YouTubeBadRequest, '403': YouTubeForbidden}

        params = self.digest_request_params(resource_filter, parts, optional_params)

        url = ENDPOINT.format(resource_type=self.resource_type)
        params.update({'key': self.api_key})
        response = requests.get(url, params=params)

        if response.status_code in ERRORS_MAPPING:
            raise ERRORS_MAPPING[response.status_code](response.json['message'])
        return response

    def digest_request_params(self, resource_filter, parts, optional_params):
        self.validate_resource_filter(resource_filter)
        self.validate_parts(parts)
        self.validate_optional_params(optional_params)

        # if validation passes
        params = {'part': ','.join(parts)}
        params.update(resource_filter)
        params.update(optional_params)

        return params

    def validate_resource_filter(self, resource_filter):
        if len(resource_filter) > 1:
            raise OneFilterAllowed('YouTube allows one filter per request only')

        _filter = resource_filter.keys()[0]
        if _filter not in self.allowed_filters:
            raise FilterNotAllowed('{0} is not an allowed filter'.format(_filter))

    def validate_parts(self, parts):
        not_allowed_parts = [part for part in parts if part not in self.allowed_parts]
        if not_allowed_parts:
            raise PartNotAllowed('{0} is not an allowed part'.format(','.join(not_allowed_parts)))

    def validate_optional_params(self, optional_params):
        not_allowed_params = [param for param in optional_params.keys() if param not in self.allowed_optional_params]
        if not_allowed_params:
            raise OptionalParamNotAllowed('{0} is not allowed params'.format(','.join(not_allowed_params)))


class VideoAPI(Client):
    """
    Videos endpoint specific client https://developers.google.com/youtube/v3/docs/videos/
    """
    def __init__(self, api_key):
        super(VideoAPI, self).__init__(api_key)
        self.resource_type = 'videos'
        self.allowed_parts = {'contentDetails': 2,
                              'fileDetails': 1,
                              'id': 0,
                              'liveStreamingDetails': 2,
                              'player': 0,
                              'processingDetails': 1,
                              'recordingDetails': 2,
                              'snippet': 2,
                              'statistics': 2,
                              'status': 2,
                              'suggestions': 1,
                              'topicDetails': 2}
        self.allowed_filters = ('chart',
                                'id',
                                'myRating')
        self.allowed_optional_params = ('maxResults',
                                        'onBehalfOfContentOwner',
                                        'pageToken',
                                        'regionCode',
                                        'videoCategoryId')

    def calculate_quota(self, parts):
        return sum((self.allowed_parts[part] for part in parts))

    def get_videos(self, resource_filter, parts, optional_params):
        """
        Get info for videos resource

        :param resource_filter: dictionary with one key:value pair only
        :param parts: tuple of strings https://developers.google.com/youtube/v3/getting-started#part
        :param optional_params: dictionary, usually filter params
        :return: serialised json response
        """
        response = self.get_resource(resource_filter, parts, optional_params=optional_params)
        return response.json

    def get_video_by_id(self, video_id, parts=('snippet',), optional_params={}):
        return self.get_videos(resource_filter={'id': video_id}, parts=parts, optional_params=optional_params)

