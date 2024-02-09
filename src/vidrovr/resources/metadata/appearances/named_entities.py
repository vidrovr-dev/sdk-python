from vidrovr.core import Client

from pydantic import BaseModel


class NamedEntitiesAppearancesModel(BaseModel):
    """
    Model of named entity appearances

    :param id: ID of the named entity appearance
    :type id: str
    :param name: Name of the named entity appearing
    :type name: str
    :param appearances: List of something
    :type appearances: list
    """

    id: str = None
    name: str = None
    appearances: list = None


class NamedEntitiesAppearances:
    @classmethod
    def read(cls, asset_id: str):
        """
        Returns an array of named entity appearances for the asset.

        :param asset_id: ID of the asset
        :type asset_id: str
        :return: Array of information for the named entities
        :rtype: list[NamedEntitiesAppearancesModel]
        """
        url = f"metadata/{asset_id}/appearances/named_entities"
        response = Client.get(url)
        named_entity = [NamedEntitiesAppearancesModel(**item) for item in response]

        return named_entity
