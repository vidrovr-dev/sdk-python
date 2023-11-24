#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Vidrovr Inc.
# By: Gianni Galbiati
import os

from functools import partial, wraps

import orjson as json
import requests

from requests.exceptions import RequestException
from vidrovr.exceptions import *

API_KEY = ''
BASE_URL = ''

API_DEFAULT_PROJECT_ID = os.environ.get('VIDROVR_DEFAULT_PROJECT_ID')
API_DOMAIN = os.environ.get('VIDROVR_API_DOMAIN', 'https://api.vidrovr.com')
API_KEY = os.environ.get('VIDROVR_API_KEY')
API_VERSION = os.environ.get('VIDROVR_API_VERSION', 'v2')

BASE_URL = f"{API_DOMAIN}/{API_VERSION}"

HEADERS = {'x-api-key': API_KEY}


def api_wrapper(method):
    # Set of methods that do not accept a JSON body consistently
    body_disallowed = {requests.get, requests.delete}

    def wrapper(f):
        @wraps(f)
        def wrapped(uri, headers: dict = None, body: dict = None, files=None):
            # Resource URL
            url = f"{BASE_URL}/{uri}"

            # Combine default headers with custom headers
            headers = HEADERS | (headers or {})

            if body is not None and files is not None:
                raise ThereCanBeOnlyOneError(f"You may not pass both a JSON request body and files.")

            if method in body_disallowed:
                raise NoBodyAllowedError(f"HTTP method {method.__name__} cannot take JSON body.")

            response = method(url, headers=headers, json=body)

            try:
                response.raise_for_status()
            except RequestException:
                # TODO: Is 'errors' the correct key here?
                return json.loads(response.content)['errors'] if response.content else None

            return json.loads(response.content)['data'] if response.content else None
        return wrapped
    return wrapper


post = api_wrapper(requests.post)
get = api_wrapper(requests.get)
patch = api_wrapper(requests.patch)
delete = api_wrapper(requests.delete)
