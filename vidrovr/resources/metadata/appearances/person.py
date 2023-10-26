from ....core import Client

from dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class PersonAppearanceData:
    asset_id: str
    name: str
    appearances: list

class PersonAppearances(BaseModel):

    @classmethod
    def read(cls, asset_id: str):
        url      = f'metadata/{asset_id}/appearances/persons'
        response = Client.get(url)
        person   = [PersonAppearanceData(**item) for item in response]

        return person