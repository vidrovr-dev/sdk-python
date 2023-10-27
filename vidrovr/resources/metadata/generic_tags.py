from ...core import Client

from dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class GenericTagData:
    asset_id: str
    name: str
    time: str
    score: float

class GenericTag(BaseModel):

    @classmethod
    def read(cls, asset_id: str, tag_id: str=None):
        """
        Returns an array of generic tag detections or information about a specific generic tag detection.
        
        :param asset_id: ID of the asset
        :type asset_id: str
        :param tag_id: ID of the tag or None
        :type tag_id: str
        :return: Array of generic tag detections or single generic tag detection
        :rtype: list[GenericTagData] or GenericTagData
        """
        if tag_id is None:
            url      = f'metadata/{asset_id}/generic_tags'
            response = Client.get(url)
        else:
            url      = f'metadata/{asset_id}/generic_tags/{tag_id}'
            response = Client.get(url)

        generic_tag = GenericTagData(
            asset_id=response['id'],
            name=response['name'],
            time=response['time'],
            score=response['score']
        )

        return generic_tag