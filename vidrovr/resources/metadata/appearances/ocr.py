from vidrovr.core import Client

from pydantic import BaseModel

class OCRAppearanceModel(BaseModel):
    """
    Model of on screen text appearances

    :param id: ID of the on screen text appearance
    :type id: str
    :param name: Name of the on screen text appearing
    :type name: str
    :param appearances: List of something
    :type appearances: list
    """
    asset_id: str = None
    text: str = None
    appearances: list = None

class OCRAppearances:

    @classmethod
    def read(cls, asset_id: str):
        """
        Returns an array of on screen text appearances for the asset.

        :param asset_id: ID of the asset
        :type asset_id: str
        :return: Array of information about the OCR appearances
        :rtype: list[OCRAppearanceModel]
        """
        url      = f'metadata/{asset_id}/appearances/ocr'
        response = Client.get(url)
        ocr      = [OCRAppearanceModel(**item) for item in response]

        return ocr