from ...core import Client

from dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class CustomTagData:
    asset_id: str
    name: str
    time: str
    score: float

class CustomTag(BaseModel):

    @classmethod
    def read(cls, asset_id: str, tag_id: str=None):
        """
        Returns an array of custom tag detections or information about a specific custom tag detection.
        
        :param asset_id: ID of the asset
        :type asset_id: str
        :param tag_id: ID of the tag or None
        :type tag_id: str
        :return: Array of custom tag detections or a single custom tag detection
        :rtype: list[CustomTagData] or CustomTagData
        """
        if tag_id is None:
            url      = f'metadata/{asset_id}/custom_tags'
            response = Client.get(url)
        else:
            url      = f'metadata/{asset_id}/custom_tags/{tag_id}'
            response = Client.get(url)

        custom_tag = CustomTagData(
            asset_id=response['id'],
            name=response['name'],
            time=response['time'],
            score=response['score']
        )

        return custom_tag