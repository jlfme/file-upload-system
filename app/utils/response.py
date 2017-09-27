#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# ---------------------------------------
# Created by: Jlfme<jlfgeek@gmail.com>
# Created on: 2017-09-26 18:37:18
# ---------------------------------------


import json
from flask import Response


MIME_ANY = '*/*'
MIME_JSON = 'application/json'
MIME_TEXT = 'text/plain'


def response_mimetype(request):
    """根据客户端的可接受mime_types返回适当的mime_type
    'Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    :param request -- a HttpRequest instance.
    """

    can_json = MIME_JSON in request.accept_mimetypes
    can_json |= MIME_ANY in request.accept_mimetypes
    return MIME_JSON if can_json else MIME_TEXT


class JSONResponse(Response):

    def __init__(self, data, mimetype=MIME_JSON, headers=None):
        response = json.dumps(data)
        super(JSONResponse, self).__init__(response=response, mimetype=mimetype, headers=headers)
