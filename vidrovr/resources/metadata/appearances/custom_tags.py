from vidrovr.core import Client

from pydantic import BaseModel

class CustomTagsAppearanceModel(BaseModel):
    """
    Model of custom tag appearances

    :param id: ID of the custom tag appearance
    :type id: str
    :param name: Name of the custom tag appearing
    :type name: str
    :param appearances: List of something
    :type appearances: list
    """
    id: str = None
    name: str = None
    appearances: list = None

class CustomTagsAppearances:

    @classmethod
    def read(cls, asset_id: str):
        """
        Returns an array of custom tag appearances for the asset.

        :param asset_id: ID of the asset
        :type asset_id: str
        :return: Array of information about the custom tag appearances
        :rtype: list[CustomTagsAppearanceModel]
        """
        url        = f'metadata/{asset_id}/appearances/custom_tags'
        response   = Client.get(url)

        if response is not None:
            custom_tag = [CustomTagsAppearanceModel(**item) for item in response]

            return custom_tag
        else:
            return response