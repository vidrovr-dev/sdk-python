from vidrovr.core import Client

from pydantic import BaseModel


class GenericTagsAppearancesModel(BaseModel):
    """
    Model of generic tag appearances

    :param id: ID of the generic tag appearance
    :type id: str
    :param name: Name of the generic tag appearing
    :type name: str
    :param appearances: List of something
    :type appearances: list
    """

    id: str = None
    name: str = None
    appearances: list = None


class GenericTagsAppearances:
    @classmethod
    def read(cls, asset_id: str):
        """
        Returns an array of generic tag appearances for the asset.

        :param asset_id: ID of the asset
        :type asset_id: str
        :return: Array of information about the generic tag appearances
        :rtype: list[GenericTagsAppearancesModel]
        """
        url = f"metadata/{asset_id}/appearances/generic_tags"
        response = Client.get(url)
        generic_tags = [GenericTagsAppearancesModel(**item) for item in response]

        return generic_tags
