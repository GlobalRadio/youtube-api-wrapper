class YouTubeForbidden(Exception):
    """
    YouTube Forbidden request encapsulation
    """
    pass


class YouTubeBadRequest(Exception):
    """
    YouTube Bad request encapsulation
    """
    pass


class YoutubeNotFound(Exception):
    """
    YouTube Not Found request encapsulation
    """
    pass


class BadParametersRequest(Exception):
    """
    Bad Parameters in the requests
    """
    pass


class PartNotAllowed(BadParametersRequest):
    """
    Request part not allowed for the resource
    """
    pass


class FilterNotAllowed(BadParametersRequest):
    """
    Filter not allowed for the resource
    """
    pass


class OneFilterAllowed(BadParametersRequest):
    """

    """
    pass


class OptionalParamNotAllowed(BadParametersRequest):
    """

    """
    pass


class BadKindOfResponse(BadParametersRequest):
    """

    """
    pass
