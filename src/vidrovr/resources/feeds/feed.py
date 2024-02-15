#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Vidrovr Inc.
# By: Gianni Galbiati

# Standard libraries
import enum

from datetime import datetime
from typing import ClassVar
from uuid import UUID

# External libraries
from pydantic import model_validator
from pydantic import AnyHttpUrl

# Internal libraries
from vidrovr.resources._base import BaseResource


class FeedTypes(enum.Enum):
    """Accepted feed type options."""

    youtube = "youtube"
    twitter_profile = "twitter_profile"
    twitter_hashtag = "twitter_hashtag"
    instagram_profile = "instagram_profile"
    instagram_hashtag = "instagram_hashtag"
    facebook_profile = "facebook_profile"

    hls = "hls"
    rtmp = "rtmp"
    rtsp = "rtsp"

    user_upload = "user_upload"

    @classmethod
    def streaming_types(cls):
        return [FeedTypes.hls, FeedTypes.rtsp, FeedTypes.rtmp]


class Feed(BaseResource):
    """Represents the feed resource."""

    route: ClassVar[str] = "feeds"
    updatable: ClassVar[list[str]] = ["name"]
    # TODO: add more ^

    type: str = "feeds"

    # Basics
    name: str
    feed_type: FeedTypes
    project_uids: list[UUID]
    is_active: bool = True
    status: str = None

    creation_date: datetime | None = None
    updated_date: datetime | None = None

    # Processing settings
    priority: int = 0

    # Extra stuff to know about the feed
    additional_metadata: dict | None = None

    # Polling feed params
    query_parameters: str | None = None
    profile: str | None = None
    hashtag: str | None = None
    polling_freq: int | None = None
    next_poll_date: datetime | None = None

    # Streaming feed params
    link: AnyHttpUrl | None = None
    segment_length: int | None = None

    @model_validator(mode="after")
    def streaming_feed_has_link(self):
        # TODO: does this break on GET?
        ft = self.feed_type
        if ft in FeedTypes.streaming_types():
            if self.link is None:
                raise ValueError(f"Link is required for feed type {ft}")

        return self
