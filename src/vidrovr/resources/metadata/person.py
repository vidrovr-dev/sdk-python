from src.vidrovr.core import Client

from pydantic import BaseModel


class PersonModel(BaseModel):
    """
    Model of person detections

    :param id: ID of the detection
    :type id: str
    :param person_id: ID of the person detected
    :type person_id: str
    :param person_name: Name of the person detected
    :type person_name: str
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
    person_id: str = None
    person_name: str = None
    time: str = None
    score: float = 0.0
    x: float = 0.0
    y: float = 0.0
    w: float = 0.0
    h: float = 0.0


class Person:
    @classmethod
    def read(cls, asset_id: str, face_id: str = None):
        """
        Returns an array of person detections or information about a specific detection

        :param asset_id: ID of the asset
        :type asset_id: str
        :param face_id: ID of the person detection or None
        :type face_id: str
        :return: Array of person detection information or detail information for a single detection
        :rtype: list[PersonModel] or PersonModel
        """
        if face_id is None:
            url = f"metadata/{asset_id}/faces"
            response = Client.get(url)
        else:
            url = f"metadata/{asset_id}/faces/{face_id}"
            response = Client.get(url)

        if response is not None:
            if isinstance(response, dict):
                person = PersonModel(
                    id=response["id"],
                    person_id=response["person_id"],
                    person_name=response["person_name"],
                    time=response["time"],
                    score=response["score"],
                    x=response["x"],
                    y=response["y"],
                    w=response["w"],
                    h=response["h"],
                )
            elif isinstance(response, list):
                person = [PersonModel(**item) for item in response]

            return person
        else:
            return response
