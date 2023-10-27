from ...core import Client

from dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class PersonData:

    id: str
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
        """
        Returns an array of person detections or information about a specific detection

        :param asset_id: ID of the asset
        :type asset_id: str
        :param face_id: ID of the person detection or None
        :type face_id: str
        :return: Array of person detection information or detail information for a single detection
        :rtype: list[PersonData] or PersonData
        """
        if face_id is None:
            url      = f'metadata/{asset_id}/faces'
            response = Client.get(url)
        else:
            url      = f'metadata/{asset_id}/faces/{face_id}'
            response = Client.get(url)

        if isinstance(response, dict):
            person = PersonData(
                id=response['id'],
                person_id=response['person_id'],
                person_name=response['person_name'],
                time=response['time'],
                score=response['score'],
                x=response['x'],
                y=response['y'],
                w=response['w'],
                h=response['h']
            )
        elif isinstance(response, list):
            person = [PersonData(**item) for item in response]

        return person