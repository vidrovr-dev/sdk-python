from ...core import Client

from dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class IABTagData:
    asset_id: str
    name: str
    time: str
    score: float

class IABTag(BaseModel):

    @classmethod
    def read(cls, asset_id: str, tag_id: str=None):
        """
        Returns an array of IAB tag detections or information about a specific IAB tag detection.
        
        :param asset_id: ID of the asset
        :type asset_id: str
        :param tag_id: ID of the tag or None
        :type tag_id: str
        :return: Array of IAB tag detections or single IAB tag detection
        :rtype: list[IABTagData] or IABTagData
        """
        if tag_id is None:
            url      = f'metadata/{asset_id}/iab_tags'
            response = Client.get(url)
        else:
            url      = f'metadata/{asset_id}/iab_tags/{tag_id}'
            response = Client.get(url)

        if isinstance(response, dict):
            iab_tag = IABTagData(
                asset_id=response['id'],
                name=response['name'],
                time=response['time'],
                score=response['score']
            )
        elif isinstance(response, list):
            iab_tag = [IABTagData(**item) for item in response]

        return iab_tag