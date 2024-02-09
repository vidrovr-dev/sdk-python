from vidrovr.core import Client

from pydantic import BaseModel


class ObjectModel(BaseModel):
    """
    Model of an object

    :param id: ID of the detection
    :type id: str
    :param label_id: ID of the object detected
    :type label_id: str
    :param label_name: Name of the object detected
    :type label_name: str
    :param time: Timestamp for the detection
    :type time: str
    :param score: Confidence score of the detection
    :type score: float
    :param x: X coordinate of the detection
    :type x: float
    :param y: Y coordinate of the detection
    :type y: float
    :param w: Width of the detection
    :type w: float
    :param h: Height of the detection
    :type h: float
    :param frame_height: Height of the asset in pixels
    :type frame_height: int
    :param frame_width: Width of the asset in pixels
    :type frame_width: int
    """

    id: str = None
    label_id: str = None
    label_name: str = None
    time: str = None
    score: float = 0.0
    x: float = 0.0
    y: float = 0.0
    w: float = 0.0
    h: float = 0.0
    frame_height: int = 0
    frame_width: int = 0


class Object:
    @classmethod
    def read(cls, asset_id: str, obj_detection_id: str = None):
        """
        Returns an array of object detections or information about a specific object detection.

        :param asset_id: ID of the asset
        :type asset_id: str
        :param obj_detection_id: ID of the object detection or None
        :type obj_detection_id: str
        :return: Array of object detections of single object detection
        :rtype: list[ObjectModel] or ObjectModel
        """
        if obj_detection_id is None:
            url = f"metadata/{asset_id}/object_detections"
            response = Client.get(url)
        else:
            url = f"metadata/{asset_id}/object_detections/{obj_detection_id}"
            response = Client.get(url)

        if response is not None:
            if isinstance(response, dict):
                obj = ObjectModel(
                    id=response["id"],
                    label_id=response["label_id"],
                    label_name=response["label_name"],
                    time=response["time"],
                    score=response["score"],
                    x=response["x"],
                    y=response["y"],
                    w=response["w"],
                    h=response["h"],
                    frame_height=response["frame_height"],
                    frame_width=response["frame_width"],
                )
            elif isinstance(response, list):
                obj = [ObjectModel(**item) for item in response]

            return obj
        else:
            return response
