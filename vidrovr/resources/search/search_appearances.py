import json

from ...core import Client

from dataclasses import dataclass
from pydantic import BaseModel
from typing import List

@dataclass
class AppearancesFeedItems:
    type: str
    field: str
    limit: int

@dataclass
class AppearancesFacet:
    feed_items: AppearancesFeedItems

@dataclass
class AppearancesFeedId:
    type: str
    field: str
    limit: int
    facet: AppearancesFacet

@dataclass
class AppearancesFacetWithFacets:
    feed_id: AppearancesFeedId

@dataclass
class SearchAppearancesData:
    project_id: str
    query: str
    filter: List[str]
    sort: str
    limit: int
    offset: int
    facet: AppearancesFacetWithFacets

class SearchAppearances(BaseModel):

    @classmethod
    def create(cls, project_id: str, data: SearchAppearancesData):
        url     = 'search/appearances'
        payload = json.dumps(data, default=lambda o: o.__dict__)
        '''payload = {
            'project_id': project_id, 
            'query': '*',
            'filter': [
                '{!join fromIndex=appearances method=crossCollection from=feed_item_id to=feed_item_id df=_text_}dog'
            ],
            'sort': 'original_time desc',
            'limit': 10,
            'offset': 0,
            'facet': {
                'feed_id': {
                    'type': 'terms',
                    'field': 'feed_id',
                    'limit': -1,
                    'facet': {
                        'feed_items': {
                            'type': 'terms',
                            'field': 'feed_item_id',
                            'limit': -1
                        }
                    }
                }
            }
        }'''
        response = Client.post(url, payload)

        return response