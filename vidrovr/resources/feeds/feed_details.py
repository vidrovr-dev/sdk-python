from ...core import Client

from dataclasses import dataclass
from pydantic import BaseModel
from icecream import ic

@dataclass
class FeedDetailData:
    type: str
    id: str
    creation_date: str
    is_active: bool
    name: str
    next_poll_date: str
    num_feed_items: str
    polling_frequency: int
    query_parameters: str
    status: str
    updated_date: str

class FeedDetail(BaseModel):

    @classmethod
    def read(cls, feed_id: str, project_id: str):
        url      = f'feeds/{feed_id}?project_uid={project_id}'
        response = Client.get(url)
        feed_detail = FeedDetailData(
            type=response['type'],
            id=response['id'],
            creation_date=response['creation_date'],
            is_active=response['is_active'],
            name=response['name'],
            next_poll_date=response['next_poll_date'],
            num_feed_items=response['num_feed_items'],
            polling_frequency=response['polling_frequency'],
            query_parameters=response['query_parameters'],
            status=response['status'],
            updated_date=response['updated_date']
        )

        return feed_detail