import json

from src.vidrovr.core import Client

from pydantic import BaseModel
from typing import List


class AppearancesFeedItems(BaseModel):
    type: str = None
    field: str = None
    limit: int = 0


class AppearancesFacet(BaseModel):
    feed_items: AppearancesFeedItems


class AppearancesFeedId(BaseModel):
    type: str = None
    field: str = None
    limit: int = 0
    facet: AppearancesFacet


class AppearancesFacetWithFacets(BaseModel):
    feed_id: AppearancesFeedId


class SearchAppearancesData(BaseModel):
    project_id: str = None
    query: str = None
    filter: List[str] = None
    sort: str = None
    limit: int = 0
    offset: int = 0
    facet: AppearancesFacetWithFacets


class SearchAppearances:
    @classmethod
    def create(cls, project_id: str, data: SearchAppearancesData):
        """
        Create an appearances search

        :param project_id: ID of the project containing the search
        :type project_id: str
        :param data: Object model containing the details of the search
        :type data: SearchAppearancesData
        """
        url = "search/appearances"
        payload = data.model_dump_json()
        response = Client.post(url, payload)

        # if response is not None:
        # do stuff
        # else:
        return response
