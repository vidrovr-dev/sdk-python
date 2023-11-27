from vidrovr.core import Client

from pydantic import BaseModel

class CustomTagModel(BaseModel):
    """
    Model of a custom tag

    :param asset_id: ID of the detection
    :type asset_id: str
    :param name: Name of the custom tag detected
    :type name: str
    :param time: Timestamp for detection of the tag
    :type time: str
    :param score: Confidence score for the detection
    :type score: float
    """
    id: str = None
    name: str = None
    time: str = None
    score: float = 0.0

class CustomTag:

    @classmethod
    def read(cls, asset_id: str, tag_id: str=None):
        """
        Returns an array of custom tag detections or information about a specific custom tag detection.
        
        :param asset_id: ID of the asset
        :type asset_id: str
        :param tag_id: ID of the tag or None
        :type tag_id: str
        :return: Array of custom tag detections or a single custom tag detection
        :rtype: list[CustomTagModel] or CustomTagModel
        """
        if tag_id is None:
            url      = f'metadata/{asset_id}/custom_tags'
            response = Client.get(url)
        else:
            url      = f'metadata/{asset_id}/custom_tags/{tag_id}'
            response = Client.get(url)

        if response is not None:
            if isinstance(response, dict):
                custom_tag = CustomTagModel(
                    id=response['id'],
                    name=response['name'],
                    time=response['time'],
                    score=response['score']
                )
            elif isinstance(response, list):
                custom_tag = [CustomTagModel(**item) for item in response]

            return custom_tag
        else:
            return response