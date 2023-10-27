from ....core import Client

from dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class GenericTagsAppearanceData:
    id: str
    name: str
    appearances: list

class GenericTagsAppearances(BaseModel):

    @classmethod
    def read(cls, asset_id: str):
        """
        Returns an array of generic tag appearances for the asset.

        :param asset_id: ID of the asset
        :type asset_id: str
        :return: Array of information about the generic tag appearances
        :rtype: list[GenericTagsAppearanceData]
        """
        url          = f'metadata/{asset_id}/appearances/generic_tags'
        response     = Client.get(url)
        generic_tags = [GenericTagsAppearanceData(**item) for item in response]

        return generic_tags