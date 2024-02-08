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
import orjson as json

from pydantic import BaseModel, AnyHttpUrl, UUID4

# Internal libraries
from vidrovr import client


class Resource(BaseModel):
    route: ClassVar[str] = ""
    id: UUID4
    type: str

    @classmethod
    def _url(cls) -> AnyHttpUrl:
        return f"{client.cfg.url}/{cls.route}"

    def url(self) -> AnyHttpUrl:
        return f"{self._url()}/{str(self.id)}"

    def create(self):
        body = self.model_dump()
        response = client.post(self.url(), data=body)
        response.raise_for_status()
        return json.loads(response.content).get("data") if response.content else None
