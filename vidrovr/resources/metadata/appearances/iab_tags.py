from vidrovr.core import Client

from pydantic import BaseModel

class IABAppearanceModel(BaseModel):
    """
    Model of IAB tag appearances

    :param id: ID of the IAB tag appearance
    :type id: str
    :param name: Name of the IAB tag appearing
    :type name: str
    :param appearances: List of something
    :type appearances: list
    """
    asset_id: str = None
    name: str = None
    appearances: list = None

class IABAppearances:

    @classmethod
    def read(cls, asset_id: str):
        """
        Returns an array of IAB tag appearances for the asset.

        :param asset_id: ID of the asset
        :type asset_id: str
        :return: Array of information about the IAB tag appearances
        :rtype: list[IABAppearanceModel]
        """
        url      = f'metadata/{asset_id}/appearances/iab_tags'
        response = Client.get(url)
        iab      = [IABAppearanceModel(**item) for item in response]

        return iab