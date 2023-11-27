from vidrovr.core import Client

from pydantic import BaseModel

class ObjectAppearanceModel(BaseModel):
    """
    Model of object appearances

    :param id: ID of the object appearance
    :type id: str
    :param name: Name of the object appearing
    :type name: str
    :param appearances: List of something
    :type appearances: list
    """
    id: str = None
    name: str = None
    appearances: list = None

class ObjectAppearances:

    @classmethod
    def read(cls, asset_id: str):
        """
        Returns an array of object appearances for the asset.

        :param asset_id: ID of the asset
        :type asset_id: str
        :return: Array of information about the object appearances
        :rtype: list[ObjectAppearanceModel]
        """
        url      = f'metadata/{asset_id}/appearances/objects'
        response = Client.get(url)
        obj      = [ObjectAppearanceModel(**item) for item in response]

        return obj