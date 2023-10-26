from ...core import Client

from dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class PersonData:

    asset_id: str
    person_id: str
    person_name: str
    time: str
    score: float
    x: float
    y: float
    w: float
    h: float

class Person(BaseModel):

    @classmethod
    def read(cls, asset_id: str, face_id: str=None):

        if face_id is None:
            url      = f'metadata/{asset_id}/faces'
            response = Client.get(url)
        else:
            url      = f'metadata/{asset_id}/faces/{face_id}'
            response = Client.get(url)

        person = PersonData(
            asset_id=response['id'],
            person_id=response['person_id'],
            person_name=response['person_name'],
            time=response['time'],
            score=response['score'],
            x=response['x'],
            y=response['y'],
            w=response['w'],
            h=response['h']
        )

        return person