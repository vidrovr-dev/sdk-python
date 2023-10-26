from ...core import Client

from dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class FeedData:
    type: str
    id: str
    name: str

@dataclass
class FeedItem:
    feed_type: str
    name: str
    media_type: str
    hls_link: str
    project_uids: str

class Feed(BaseModel):

    @classmethod
    def read(cls, project_id: str):
        url      = f'feeds/?project_uid={project_id}'
        response = Client.get(url)

        if isinstance(response, dict):
            feed_object = FeedData(
                type=response['type'],
                id=response['id'],
                name=response['name']
            )
        elif isinstance(response, list):
            feed_object = [FeedData(**item) for item in response]

        return feed_object
    
    @classmethod
    def delete(cls, feed_id: str, project_id: str):
        url      = f'feeds/{feed_id}?project_uid={project_id}'
        response = Client.delete(url)

        return response
    
    @classmethod
    def update(cls, feed_id: str, project_id: str, status: str):
        url = f'feeds/{feed_id}'
        payload = {
            'data': {
                'is_active': status,
                'project_uids': project_id
            }
        }
        response = Client.patch(url, payload)

        return response
    
    @classmethod
    def create(cls, data: FeedItem):
        url     = 'feeds/'
        payload = {
            'data': {
                'feed_type': data.feed_type,
                'name': data.name,
                'media_type': data.media_type,
                'hls_link': data.hls_link,
                'project_uids': [data.project_uids]
            }
        }
        response = Client.post(url, payload)

        return response