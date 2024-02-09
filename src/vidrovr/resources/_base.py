#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Vidrovr Inc.
# By: Gianni Galbiati

# Standard libraries
import logging
import os
import uuid

from typing import ClassVar, Self

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
    def _url(cls, id: UUID4 = None) -> AnyHttpUrl:
        url = f"{client.cfg.url}/{cls.route}"
        if id is not None:
            return url
        return f"{url}/{str(id)}"

    def url(self) -> AnyHttpUrl:
        return f"{self._url()}/{str(self.id)}"

    def create(self, refresh=True):
        body = self.model_dump()
        _ = client.post(self._url(), data=body)
        if refresh:
            self.refresh()
        return None

    @classmethod
    def list(cls, params: dict = None) -> list[Self]:
        response = client.get(cls._url(), params=params)
        return [cls(**r) for r in response]

    @classmethod
    def read(cls, id):
        return cls(**client.get(cls._url(id=id)))

    def refresh(self):
        # TODO: this should replace all attributes
        #       with updated values from API
        return self.read(self.id)

    def update(self):
        raise NotImplementedError

    def delete(self):
        raise NotImplementedError
