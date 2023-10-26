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

        if tag_id is None:
            url      = f'metadata/{asset_id}/iab_tags'
            response = Client.get(url)
        else:
            url      = f'metadata/{asset_id}/iab_tags/{tag_id}'
            response = Client.get(url)

        iab_tag = IABTagData(
            asset_id=response['id'],
            name=response['name'],
            time=response['time'],
            score=response['score']
        )

        return iab_tag