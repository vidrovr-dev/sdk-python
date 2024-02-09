#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Vidrovr Inc.
# By: Gianni Galbiati

# Standard libraries
from datetime import datetime
from uuid import UUID

# External libraries
from pydantic import field_validator, Field
from pydantic import AnyHttpUrl

# Internal libraries
from vidrovr.resources._base import BaseResource


class Feed(BaseResource):
    type: str = "feeds"

    # Basics
    name: str
    project_uids: list[UUID]
    is_active: bool = True
    status: str = None

    creation_date: datetime | None
    updated_date: datetime | None

    # Processing settings
    priority: int = 0
    segment_length: int | None

    # Polling and continuous feed params
    link: AnyHttpUrl | None
    query_parameters: str | None
    profile: str | None
    hashtag: str | None

    polling_freq: int | None
    next_poll_date: datetime | None

    # Extra stuff to know about the feed
    additional_metadata: dict | None
