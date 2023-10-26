from ....core import Client

from dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class NamedEntitiesAppearanceData:
    id: str
    name: str
    appearances: list

class NamedEntitiesAppearances(BaseModel):

    @classmethod
    def read(cls, asset_id: str):
        url          = f'metadata/{asset_id}/appearances/named_entities'
        response     = Client.get(url)
        named_entity = [NamedEntitiesAppearanceData(**item) for item in response]

        return named_entity