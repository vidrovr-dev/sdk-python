#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Vidrovr Inc.
# By: Gianni Galbiati

# Standard libraries
from typing import ClassVar, Self
from uuid import UUID

# External libraries
from pydantic import BaseModel, AnyHttpUrl

# Internal libraries
from vidrovr import client


class Resource(BaseModel):
    """Base class with shared methods for CRUD on remote resources.

    Attributes:
        route (str): a non-model attribute used to link the resource to a URI
        updatable (list[str]): a list of model fields accepted by `update` method
        id (UUID): an identifier for the resource
        type (str): the name of the resource's type, as provided by the API
    """

    route: ClassVar[str] = ""
    updatable: ClassVar[list[str]] = []

    id: UUID
    type: str

    @classmethod
    def _url(cls, id: UUID = None) -> AnyHttpUrl:
        """Return the base URL for the resource, optionally with identifier."""
        url = f"{client.cfg.url}/{cls.route}"
        if id is not None:
            return url
        return f"{url}/{str(id)}"

    def url(self) -> AnyHttpUrl:
        """Return the URL for the resource, including the identifier."""
        return f"{self._url()}/{str(self.id)}"

    def body(self, for_update: bool = False) -> dict:
        """Return a JSON-serializable dictionary from the model."""
        dump = self.model_dump(exclude_unset=True)

        if for_update:
            dump = {k: v for k, v in dump.items() if k in self.updatable}

        return {"data": dump}

    def create(self, refresh: bool = True):
        """Send a post request to create the remote resource from the model."""
        client.post(self._url(), data=self.body())

        if refresh:
            self.refresh()

        return None

    @classmethod
    def list(cls, params: dict = None) -> list[Self]:
        """Retrieve a list of identifier model stubs for the resource."""
        response = client.get(cls._url(), params=params)
        return [cls(**r) for r in response]

    @classmethod
    def read(cls, id: UUID) -> Self:
        """Retrieve the resource by ID and construct the model."""
        return cls(**client.get(cls._url(id=id)))

    def refresh(self):
        """Re-read all data from the resource for the model."""
        self.__init__(**client.get(self._url(id=self.id)))
        return None

    def update(self, refresh: bool = True):
        """Update the resource based on the model."""
        client.patch(self.url(), data=self.body(for_update=True))

        if refresh:
            self.refresh()

        return None

    def delete(self):
        """Delete the remote resource by ID."""
        client.delete(self.url())
        return None
