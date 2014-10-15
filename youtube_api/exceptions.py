class YouTubeForbidden(Exception):
    pass

class YouTubeBadRequest(Exception):
    pass

class BadParametersRequest(Exception):
    pass

class PartNotAllowed(BadParametersRequest):
    pass

class FilterNotAllowed(BadParametersRequest):
    pass

class OneFilterAllowed(BadParametersRequest):
    pass

class OptionalParamNotAllowed(BadParametersRequest):
    pass
