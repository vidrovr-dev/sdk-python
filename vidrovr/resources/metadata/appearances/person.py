from ....core import Client

from dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class PersonAppearanceData:
    asset_id: str
    name: str
    appearances: list

class PersonAppearances(BaseModel):

    @classmethod
    def read(cls, asset_id: str):
        """
        Returns an array of person appearances for the asset.

        :param asset_id: ID of the asset
        :type asset_id: str
        :return: Array of information about the person appearances in the asset
        :rtype: list[PersonAppearanceData]
        """
        url      = f'metadata/{asset_id}/appearances/persons'
        response = Client.get(url)
        person   = [PersonAppearanceData(**item) for item in response]

        return person