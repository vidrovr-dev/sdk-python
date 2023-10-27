from ....core import Client

from dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class IABAppearanceData:
    asset_id: str
    name: str
    appearances: list

class IABAppearances(BaseModel):

    @classmethod
    def read(cls, asset_id: str):
        """
        Returns an array of IAB tag appearances for the asset.

        :param asset_id: ID of the asset
        :type asset_id: str
        :return: Array of information about the IAB tag appearances
        :rtype: list[IABAppearanceData]
        """
        url      = f'metadata/{asset_id}/appearances/iab_tags'
        response = Client.get(url)
        iab      = [IABAppearanceData(**item) for item in response]

        return iab