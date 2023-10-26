from ....core import Client

from dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class GenericTagsAppearanceData:
    id: str
    name: str
    appearances: list

class GenericTagsAppearances(BaseModel):

    @classmethod
    def read(cls, asset_id: str):
        url          = f'metadata/{asset_id}/appearances/generic_tags'
        response     = Client.get(url)
        generic_tags = [GenericTagsAppearanceData(**item) for item in response]

        return generic_tags