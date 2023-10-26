from ...core import Client

from dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class OCRData:
    asset_id: str
    text: str
    time: str
    score: float
    x: float
    y: float
    w: float
    h: float

class OCR(BaseModel):

    @classmethod
    def read(cls, asset_id: str, appearance_id: str=None):

        if appearance_id is None:
            url      = f'metadata/{asset_id}/ocr'
            response = Client.get(url)
        else:
            url      = f'metadata/{asset_id}/ocr/{appearance_id}'
            response = Client.get(url)

        ocr = OCRData(
            asset_id=response['id'],
            text=response['text'],
            time=response['time'],
            score=response['score'],
            x=response['x'],
            y=response['y'],
            w=response['w'],
            h=response['h']
        )

        return ocr