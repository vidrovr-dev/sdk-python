from vidrovr.core import Client

from pydantic import BaseModel


class NamedEntitiesModel(BaseModel):
    """
    Model of named entities

    :param id: ID of the named entity
    :type id: str
    :param name: Name of the entity detected
    :type name: str
    :param entity_type: Type of named entity detected
    :type entity_type: str
    :param time: Timestamp for the detection
    :type time: str
    :param score: Confidence score for the detection
    :type score: float
    """

    id: str = None
    name: str = None
    entity_type: str = None
    time: str = None
    score: float = 0.0


class NamedEntities:
    @classmethod
    def read(cls, asset_id: str, entity_id: str = None):
        """
        Returns an array of named entities or information about a specific named entity.

        :param asset_id: ID of the asset
        :type asset_id: str
        :param entity_id: ID of the named entity or None
        :type entity_id: str
        :return: Array of named entities or single named entity
        :rtype: list[NamedEntitiesModel] or NamedEntitiesModel
        """
        if entity_id is None:
            url = f"metadata/{asset_id}/named_entities"
            response = Client.get(url)
        else:
            url = f"metadata/{asset_id}/named_entities/{entity_id}"
            response = Client.get(url)

        if response is not None:
            if isinstance(response, dict):
                named_entity = NamedEntitiesModel(
                    id=response["id"],
                    name=response["name"],
                    entity_type=response["entity_type"],
                    time=response["time"],
                    score=response["score"],
                )
            elif isinstance(response, list):
                named_entity = [NamedEntitiesModel(**item) for item in response]

            return named_entity
        else:
            return response
