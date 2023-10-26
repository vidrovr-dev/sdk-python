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
        url      = f'metadata/{asset_id}/appearances/ocr'
        response = Client.get(url)
        ocr      = [OCRAppearanceData(**item) for item in response]

        return ocr