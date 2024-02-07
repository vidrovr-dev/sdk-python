from vidrovr.core import Client

from pydantic import BaseModel

class OCRModel(BaseModel):
    """
    Model of on screen text

    :param id: ID of the detection
    :type id: str
    :param text: Text that was detected
    :type text: str
    :param time: Timestamp for the detection
    :type time: str
    :param score: Confidence score for the detection
    :type score: float
    :param x: X coordinate of the detection
    :type x: float
    :param y: Y coordinate of the detection
    :type y: float
    :param w: Width of the detection
    :type w: float
    :param h: Height of the detection
    :type h: float
    """
    id: str = None
    text: str = None
    time: str = None
    score: float = 0.0
    x: float = 0.0
    y: float = 0.0
    w: float = 0.0
    h: float = 0.0

class OCR:

    @classmethod
    def read(cls, asset_id: str, appearance_id: str=None):
        """
        Returns an array of OCR detections or details about a specific OCR detection.

        :param asset_id: ID of the asset
        :type asset_id: str
        :param appearance_id: ID of the OCR detection or None
        :type appearance_id: str
        :return: Array of OCR detections or single detection item
        :rtype: list[OCRModel] or OCRModel
        """
        if appearance_id is None:
            url      = f'metadata/{asset_id}/ocr'
            response = Client.get(url)
        else:
            url      = f'metadata/{asset_id}/ocr/{appearance_id}'
            response = Client.get(url)

        if response is not None:
            if isinstance(response, dict):
                ocr = OCRModel(
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
                ocr = [OCRModel(**item) for item in response]

            return ocr
        else:
            return response