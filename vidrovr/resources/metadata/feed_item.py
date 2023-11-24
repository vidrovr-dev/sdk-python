from vidrovr.client import Client

from dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class FeedItemData:

    creation_date: str
    duration: float
    feed_id: str
    fps: float
    height: int
    asset_id: str
    media_url: str
    mime_type: str
    processing_info: str
    thumbnail: str
    title: str
    width: int

class FeedItem(BaseModel):

    @classmethod
    def read(cls, asset_id: str):
        """
        Retrieve general details about a specific asset.
        
        :param asset_id: ID of the asset
        :type asset_id: str
        :return: Information about the asset
        :rtype: FeedItemData
        """
        url       = f'metadata/{asset_id}'
        response  = Client.get(url)
        feed_item = FeedItemData(
            creation_date=response['creation_date'],
            duration=response['duration'],
            feed_id=response['feed_id'],
            fps=response['fps'],
            height=response['height'],
            asset_id=response['id'],
            media_url=response['media_url'],
            mime_type=response['mime_type'],
            processing_info=response['processing_info'],
            thumbnail=response['thumbnail'],
            title=response['title'],
            width=response['width']
        )

        return feed_item