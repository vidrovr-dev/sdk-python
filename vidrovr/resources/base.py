#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Vidrovr Inc.
# By: Gianni Galbiati

from abc import ABC, abstractmethod
from functools import partial
from typing import Self
from uuid import UUID, uuid4

import orjson as json

from pydantic import BaseModel, Field
from pydantic.json import pydantic_encoder

from vidrovr import client


dumps = partial(json.dumps, default=pydantic_encoder)


class Resource(BaseModel, ABC):
    id: UUID = Field(default_factory=uuid4)

    class Config:
        validate_assignment = True

    @classmethod
    @abstractmethod
    def uri(cls, identifier: str | UUID = None) -> str:
        raise NotImplementedError

    @abstractmethod
    def create(self) -> Self:
        uri = self.uri()
        data = client.post(uri, body=self._to_body())
        return self.__class__.read(data.get('id'))

    @classmethod
    def read(cls, identifier: str | UUID) -> Self:
        uri = cls.uri(identifier)
        data = client.get(uri)
        return cls(**data)

    @abstractmethod
    def update(self) -> Self:
        body = self._to_body()
        client.patch(Resource.uri(self.id), body=body)
        return self

    @abstractmethod
    def delete(self) -> Self:
        client.delete(Resource.uri(self.id))
        return self

    def _to_body(self):
        return dumps({'data': self.dict(exclude={'id'}, exclude_none=True, exclude_unset=True)})
