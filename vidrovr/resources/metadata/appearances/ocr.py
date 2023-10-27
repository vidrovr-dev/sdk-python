from ....core import Client

from dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class OCRAppearanceData:
    asset_id: str
    text: str
    appearances: list

class OCRAppearances(BaseModel):

    @classmethod
    def read(cls, asset_id: str):
        """
        Returns an array of on screen text appearances for the asset.

        :param asset_id: ID of the asset
        :type asset_id: str
        :return: Array of information about the OCR appearances
        :rtype: list[OCRAppearanceData]
        """
        url      = f'metadata/{asset_id}/appearances/ocr'
        response = Client.get(url)
        ocr      = [OCRAppearanceData(**item) for item in response]

        return ocr