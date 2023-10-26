from ...core import Client

from dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class ObjectData:
    asset_id: str
    label_id: str
    label_name: str
    time: str
    score: float
    x: float
    y: float
    w: float
    h: float
    frame_height: int
    frame_width: int

class Object(BaseModel):

    @classmethod
    def read(cls, asset_id: str, obj_detection_id: str=None):

        if obj_detection_id is None:
            url      = f'metadata/{asset_id}/object_detections'
            response = Client.get(url)
        else:
            url      = f'metadata/{asset_id}/object_detections/{obj_detection_id}'
            response = Client.get(url)

        obj = ObjectData(
            asset_id=response['id'],
            label_id=response['label_id'],
            label_name=response['label_name'],
            time=response['time'],
            score=response['score'],
            x=response['x'],
            y=response['y'],
            w=response['w'],
            h=response['h'],
            frame_height=response['frame_height'],
            frame_width=response['frame_width']
        )

        return obj