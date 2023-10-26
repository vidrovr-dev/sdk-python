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