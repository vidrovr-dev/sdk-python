import json

from ...core import Client

from dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class SearchFeedItems:
    type: str
    field: str

@dataclass
class SearchFacet:
    feed_items: SearchFeedItems

@dataclass
class SearchQuery:
    project_id: str
    query: str
    sort: str
    limit: int
    offset: int
    facet: SearchFacet

@dataclass
class SearchData:
    name: str
    query: SearchQuery
    collection: str = 'appearances'

@dataclass
class SavedSearch:
    data: SearchData

class Search(BaseModel):

    @classmethod
    def read(cls, project_id: str, search_id: str):
        if search_id is None:
            url = f'search/saved/{project_id}'
        else:
            url = f'search/saved/{project_id}/{search_id}'

        response = Client.get(url)

        return response

    @classmethod
    def delete(cls, project_id: str, search_id: str):
        url      = f'search/saved/{project_id}/{search_id}'
        response = Client.delete(url)

        return response

    @classmethod
    def update(cls, project_id: str, search_id: str, data: SavedSearch):
        url          = f'search/saved/{project_id}/{search_id}'
        payload_json = json.dumps(data, default=lambda o: o.__dict__)

        # when updating a saved search, we don't need the collection attribute
        # so strip it out before sending the request
        payload  = cls._exclude_collection(payload_json)
        response = Client.patch(url, payload)

        return response

    @classmethod
    def create(cls, project_id: str, data: SavedSearch):
        url      = f'search/saved/{project_id}'
        payload  = json.dumps(data, default=lambda o: o.__dict__)
        response = Client.post(url, payload)

        return response
    
    def _exclude_collection(cls, data):
        data_dict = json.loads(data)
        value     = data_dict['data']['collection'] if 'collection' in data_dict.get('data', {}) else None

        # make sure we got a value from the collection key
        if value is not None:
            if 'data' in data_dict and 'collection' in data_dict['data']:
                data_dict['data'].pop('collection')

        modified_payload = json.dumps(data_dict)

        return json.dumps(modified_payload)