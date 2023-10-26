from ....core import Client

from dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class CustomTagsAppearanceData:
    id: str
    name: str
    appearances: list

class CustomTagsAppearances(BaseModel):

    @classmethod
    def read(cls, asset_id: str):
        url        = f'metadata/{asset_id}/appearances/custom_tags'
        response   = Client.get(url)
        custom_tag = [CustomTagsAppearanceData(**item) for item in response]

        return custom_tag