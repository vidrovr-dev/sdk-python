#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Vidrovr Inc.
# By: Gianni Galbiati

# Standard libraries
import logging
import os
import uuid

# External libraries
from pydantic import BaseModel, AnyHttpUrl, field_validator

# Internal libraries


class Config(BaseModel):
    url: AnyHttpUrl
    key: uuid.UUID | None

    @classmethod
    def from_env(cls):
        url = os.environ.get("VIDROVR_API_URL", "https://api.vidrovr.com")
        key = os.environ.get("VIDROVR_API_KEY")

        cfg = cls(
            url=url,
            key=key
        )

        return cfg

    @field_validator("key")
    def warn_if_not_set(cls, v):
        if v is None:
            logging.warning("VIDROVR_API_KEY not found in env vars!")

        return v
