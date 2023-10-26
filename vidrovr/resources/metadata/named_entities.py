from ...core import Client

from dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class NamedEntitiesData:
    asset_id: str
    name: str
    entity_type: str
    time: str
    score: float

class NamedEntities(BaseModel):

    @classmethod
    def read(cls, asset_id: str, entity_id: str=None):

        if entity_id is None:
            url      = f'metadata/{asset_id}/named_entities'
            response = Client.get(url)
        else:
            url      = f'metadata/{asset_id}/named_entities/{entity_id}'
            response = Client.get(url)

        named_entity = NamedEntitiesData(
            asset_id=response['id'],
            name=response['name'],
            entity_type=response['entity_type'],
            time=response['time'],
            score=response['score']
        )

        return named_entity