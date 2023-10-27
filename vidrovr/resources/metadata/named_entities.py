from ...core import Client

from dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class NamedEntitiesData:
    id: str
    name: str
    entity_type: str
    time: str
    score: float

class NamedEntities(BaseModel):

    @classmethod
    def read(cls, asset_id: str, entity_id: str=None):
        """
        Returns an array of named entities or information about a specific named entity.
        
        :param asset_id: ID of the asset
        :type asset_id: str
        :param entity_id: ID of the named entity or None
        :type entity_id: str
        :return: Array of named entities or single named entity
        :rtype: list[NamedEntitiesData] or NamedEntitiesData
        """
        if entity_id is None:
            url      = f'metadata/{asset_id}/named_entities'
            response = Client.get(url)
        else:
            url      = f'metadata/{asset_id}/named_entities/{entity_id}'
            response = Client.get(url)

        if isinstance(response, dict):
            named_entity = NamedEntitiesData(
                id=response['id'],
                name=response['name'],
                entity_type=response['entity_type'],
                time=response['time'],
                score=response['score']
            )
        elif isinstance(response, list):
            named_entity = [NamedEntitiesData(**item) for item in response]

        return named_entity