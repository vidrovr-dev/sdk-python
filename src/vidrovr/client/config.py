#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Vidrovr Inc.
# By: Gianni Galbiati

# Standard libraries
import logging
import os
import uuid

from typing import ClassVar

# External libraries
import requests

from pydantic import BaseModel, AnyHttpUrl, field_validator

# Internal libraries


class Config(BaseModel):
    """Wrap configuration and provide related conveniences."""
    # TODO: use `contextvar` to make sure this gets created per-thread?
    # Non-model class attributes
    _session: ClassVar[requests.Session] = None

    # Model fields
    url: AnyHttpUrl
    key: uuid.UUID | None

    @classmethod
    def from_env(cls):
        url = os.environ.get("VIDROVR_API_URL", "https://api.vidrovr.com")
        key = os.environ.get("VIDROVR_API_KEY")

        cfg = cls(url=url, key=key)
        cfg.refresh_session()

        return cfg

    def get_session(self):
        """Return shared requests session."""
        if self._session is None:
            self.refresh_session()
        return self._session

    def refresh_session(self):
        """Create new requests session with default headers."""
        session = requests.Session()
        session.headers.update(self.default_headers())
        self.__class__._session = session
        return self.session()

    def default_headers(self):
        """Return default headers based on configured values."""
        headers = {
            "x-api-key": self.key,
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Connection": "keep-alive"
        }
        return headers

    @field_validator("key")
    def warn_if_not_set(cls, v):
        """Warn user that their key is not set."""
        if v is None:
            logging.warning("VIDROVR_API_KEY not found in env vars!")

        return v
