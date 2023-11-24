#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Vidrovr Inc.
# By: Gianni Galbiati


class MissingAPIKeyError(EnvironmentError):
    """Raise this when the API key is not provided."""
    pass


class ThereCanBeOnlyOneError(ValueError):
    """Raise this if user tries to pass both files and JSON in a single request."""
    pass


class NoBodyAllowedError(ValueError):
    """Raise this if user tries to pass a body for a GET/DELETE request."""
    pass
