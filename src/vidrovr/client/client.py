#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Vidrovr Inc.
# By: Gianni Galbiati

# Standard libraries
from functools import wraps

# External libraries
import orjson as json

# Internal libraries
from vidrovr.client.config import Config


cfg = Config.from_env()
session = cfg.get_session()


def requestor(f):
    """Transform a requests method with default headers and response unpacking."""
    @wraps(f)
    def wrapped(*args, **kwargs):
        # Execute the request
        response = f(*args, **kwargs)

        # Raise if not 200
        response.raise_for_status()

        # Unpack data if any
        return json.loads(response.content).get("data") if response.content else None
    return wrapped


post = requestor(session.post)
get = requestor(session.get)
patch = requestor(session.patch)
delete = requestor(session.delete)
