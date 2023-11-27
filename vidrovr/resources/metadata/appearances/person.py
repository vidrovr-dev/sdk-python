from vidrovr.core import Client

from pydantic import BaseModel

class PersonAppearanceModel(BaseModel):
    """
    Model of person appearances

    :param id: ID of the person appearance
    :type id: str
    :param name: Name of the person appearing
    :type name: str
    :param appearances: List of something
    :type appearances: list
    """
    asset_id: str = None
    name: str = None
    appearances: list = None

class PersonAppearances:

    @classmethod
    def read(cls, asset_id: str):
        """
        Returns an array of person appearances for the asset.

        :param asset_id: ID of the asset
        :type asset_id: str
        :return: Array of information about the person appearances in the asset
        :rtype: list[PersonAppearanceModel]
        """
        url      = f'metadata/{asset_id}/appearances/persons'
        response = Client.get(url)
        person   = [PersonAppearanceModel(**item) for item in response]

        return person