from ...core import Client

from dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class OCRData:
    id: str
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
        """
        Returns an array of OCR detections or details about a specific OCR detection.

        :param asset_id: ID of the asset
        :type asset_id: str
        :param appearance_id: ID of the OCR detection or None
        :type appearance_id: str
        :return: Array of OCR detections or single detection item
        :rtype: list[OCRData] or OCRData
        """
        if appearance_id is None:
            url      = f'metadata/{asset_id}/ocr'
            response = Client.get(url)
        else:
            url      = f'metadata/{asset_id}/ocr/{appearance_id}'
            response = Client.get(url)

        if isinstance(response, dict):
            ocr = OCRData(
                id=response['id'],
                text=response['text'],
                time=response['time'],
                score=response['score'],
                x=response['x'],
                y=response['y'],
                w=response['w'],
                h=response['h']
            )
        elif isinstance(response, list):
            ocr = [OCRData(**item) for item in response]

        return ocr