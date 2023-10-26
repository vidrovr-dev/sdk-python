from ....core import Client

from dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class ObjectAppearanceData:
    id: str
    name: str
    appearances: list

class ObjectAppearances(BaseModel):

    @classmethod
    def read(cls, asset_id: str):
        url      = f'metadata/{asset_id}/appearances/objects'
        response = Client.get(url)
        obj      = [ObjectAppearanceData(**item) for item in response]

        return obj