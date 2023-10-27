from ....core import Client

from dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class CustomTagsAppearanceData:
    id: str
    name: str
    appearances: list

class CustomTagsAppearances(BaseModel):

    @classmethod
    def read(cls, asset_id: str):
        """
        Returns an array of custom tag appearances for the asset.

        :param asset_id: ID of the asset
        :type asset_id: str
        :return: Array of information about the custom tag appearances
        :rtype: list[CustomTagsAppearanceData]
        """
        url        = f'metadata/{asset_id}/appearances/custom_tags'
        response   = Client.get(url)
        custom_tag = [CustomTagsAppearanceData(**item) for item in response]

        return custom_tag