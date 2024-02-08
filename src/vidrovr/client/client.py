#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Vidrovr Inc.
# By: Gianni Galbiati

# Standard libraries
import logging
import os
import uuid

from functools import wraps

# External libraries
import orjson as json
import requests

# Internal libraries
from vidrovr.client.config import Config


cfg = Config.from_env()

HEADERS = {
    "x-api-key": cfg.key,
    "Accept": "application/json"
}


def requestor(f):
    """Transform a requests method with default headers and response unpacking."""
    @wraps(f)
    def wrapped(*args, **kwargs):
        # If any headers are passed, merge them with the defaults
        kwargs['headers'] = HEADERS | kwargs.pop("headers", {})

        # Execute the request
        response = f(*args, **kwargs)
        
        # Raise if not 200
        response.raise_for_status()

        # Unpack data if any
        return json.loads(response.content).get("data") if response.content else None
    return wrapped


post = requestor(requests.post)
get = requestor(requests.get)
patch = requestor(requests.patch)
delete = requestor(requests.delete)
