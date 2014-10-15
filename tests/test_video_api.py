import pytest

from youtube_api.client import VideoAPI
from youtube_api.exceptions import *

from mock import patch


@pytest.mark.parametrize(('resource_filter', 'parts', 'optional_params', 'expected_exception'), [
    ({'id': 1},            ('test',),    {},              PartNotAllowed),
    ({'test': 1},          ('snippet',), {},              FilterNotAllowed),
    ({'id': 1, 'test': 1}, ('snippet',), {},              OneFilterAllowed),
    ({'id': 1},            ('snippet',), {'test': False}, OptionalParamNotAllowed)
])
def test_query_parameters_validation(resource_filter, parts, optional_params, expected_exception):
    client = VideoAPI('api_key')
    with pytest.raises(expected_exception):
        client.digest_request_params(resource_filter, parts, optional_params)


def test_quota():
    client = VideoAPI('api_key')
    client.allowed_parts = {'test_key': 10, 'test_key2': 4, 'test_key3': 6}
    assert client.calculate_quota(('test_key2', 'test_key3')) == 10
