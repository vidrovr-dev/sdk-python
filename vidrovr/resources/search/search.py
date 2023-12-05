import json

from vidrovr.core import Client

from pydantic import BaseModel, ValidationError, validator
from icecream import ic

class SearchFeedItems(BaseModel):
    type: str = None
    field: str = None

    @validator("type", pre=True)
    def check_type(cls, value):
        if value is None:
            value = 'Default'

        return value

    @validator("field", pre=True)
    def check_field(cls, value):
        if value is None:
            value = 'Default'

        return value

class SearchFacet(BaseModel):
    feed_items: SearchFeedItems

class SearchQuery(BaseModel):
    project_id: str = None
    query: str = None
    sort: str = None
    limit: int = 0
    offset: int = 0
    facet: SearchFacet

    @validator("query", pre=True)
    def check_query(cls, value):
        if value is None:
            value = 'Default'

        return value

    @validator("sort", pre=True)
    def check_sort(cls, value):
        if value is None:
            value = 'Default'

        return value

class SearchData(BaseModel):
    name: str = None
    query: SearchQuery
    collection: str = 'appearances'

class SavedSearch(BaseModel):
    search_id: str = None
    data: SearchData

    @validator("search_id", pre=True)
    def check_search_id(cls, value):
        if value is None:
            value = 'Default'

        return value

class Search:

    @classmethod
    def read(cls, project_id: str, search_id: str = None):
        """
        Retrieve the results of a saved search

        :param project_id: ID of the project containing the saved search
        :type project_id: str
        :param search_id: ID of the saved search
        :type search_id: str
        :return: A list of saved searches
        :rtype: list[SavedSearch]
        """
        if search_id is None:
            url = f'search/saved/{project_id}'
        else:
            url = f'search/saved/{project_id}/{search_id}'

        response = Client.get(url)
        searches = []

        if response is not None:
            for item in response:
                try:
                    searchFeedItems = SearchFeedItems(
                        type=None,
                        field=None
                    )
                    searchFacet = SearchFacet(
                        feed_items=searchFeedItems
                    )
                    searchQuery = SearchQuery(
                        project_id=project_id,
                        query=None,
                        sort=None,
                        limit=0,
                        offset=0,
                        facet=searchFacet
                    )
                    searchData = SearchData(
                        name=item['name'],
                        query=searchQuery,
                        collection='appearances'
                    )
                    savedSearch = SavedSearch(
                        search_id=item['id'],
                        data=searchData
                    )

                    searches.append(savedSearch)

                except ValidationError as e:
                    print(f'Search.read(): Validation error for {item}: {e}')

            return searches
        else:
            return response

    @classmethod
    def delete(cls, project_id: str, search_id: str):
        """
        Delete a saved search

        :param project_id: ID of the project containing the saved search
        :type project_id: str
        :param search_id: ID of the saved search to delete
        :type search_id: str
        """
        ic('delete')
        url = f'search/saved/{project_id}/{search_id}'
        response = Client.delete(url)
        
        return response

    @classmethod
    def update(cls, project_id: str, search_id: str, data: SavedSearch):
        """
        Update a saved search

        :param project_id: ID of the project containing the saved search
        :type project_id: str
        :param search_id: ID of the saved search to update
        :type search_id: str
        :param data: Data model to use to update the saved search
        :type data: SavedSearch
        """
        url = f'search/saved/{project_id}/{search_id}'
        data_json = data.model_dump_json()

        # when updating a saved search, we don't need the collection key
        # so strip it out before sending the request
        payload = cls._exclude_collection(data_json, 'collection')
        response = Client.patch(url, payload)

        if response is not None:
            searchFeedItems = SearchFeedItems(
                type=None,
                field=None
            )
            searchFacet = SearchFacet(
                feed_items=searchFeedItems
            )
            searchQuery = SearchQuery(
                project_id=project_id,
                query=None,
                sort=None,
                limit=0,
                offset=0,
                facet=searchFacet
            )
            searchData = SearchData(
                name=response['name'],
                query=searchQuery,
                collection='appearances'
            )
            savedSearch = SavedSearch(
                search_id=response['id'],
                data=searchData
            )

            return savedSearch
        else:
            return response

    @classmethod
    def create(cls, project_id: str, data: SavedSearch):
        """
        Create a saved search

        :param project_id: ID of the project to contain the saved search
        :type project_id: str
        :param data: Data model to use for creating the saved search
        :type data: SavedSearch
        :return: A saved search data model on success
        :rtype: SavedSearch
        """
        url = f'search/saved/{project_id}'
        data_json = data.model_dump_json()

        # when creating a saved search, we don't need the search_id key
        # so strip it out before sending the request
        payload = cls._exclude_collection(data_json, 'search_id')
        response = Client.post(url, payload)

        if response is not None:
            searchFeedItems = SearchFeedItems(
                type=None,
                field=None
            )
            searchFacet = SearchFacet(
                feed_items=searchFeedItems
            )
            searchQuery = SearchQuery(
                project_id=project_id,
                query=None,
                sort=None,
                limit=0,
                offset=0,
                facet=searchFacet
            )
            searchData = SearchData(
                name=response['name'],
                query=searchQuery,
                collection='appearances'
            )
            savedSearch = SavedSearch(
                search_id=response['id'],
                data=searchData
            )

            return savedSearch
        else:
            return response
    
    def _exclude_collection(data, param: str):
        data_dict = json.loads(data)
        
        # remove the collection key if we're updating the search
        if param == 'collection':
            value = data_dict['data']['collection'] if 'collection' in data_dict.get('data', {}) else None

            # make sure we got a value from the collection key
            if value is not None:
                if 'data' in data_dict and 'collection' in data_dict['data']:
                    data_dict['data'].pop('collection')
        # remove the search_id key if we're creating
        elif param == 'search_id':
            value = data_dict['search_id'] if 'search_id' in data_dict else None

            if value is not None:
                ic(value)
                if 'search_id' in data_dict:
                    del data_dict['search_id']

        return data_dict