from src.vidrovr.core import Client

from pydantic import BaseModel


class GenericTagModel(BaseModel):
    """
    Model of a generic tag

    :param asset_id: ID of the detection
    :type asset_id: str
    :param name: Name of the generic tag detected
    :type name: str
    :param time: Timestamp for detection of the tag
    :type time: str
    :param score: Confidence score of the detection
    :type score: float
    """

    id: str = None
    name: str = None
    time: str = None
    score: float = 0.0


class GenericTag:
    @classmethod
    def read(cls, asset_id: str, tag_id: str = None):
        """
        Returns an array of generic tag detections or information about a specific generic tag detection.

        :param asset_id: ID of the asset
        :type asset_id: str
        :param tag_id: ID of the tag or None
        :type tag_id: str
        :return: Array of generic tag detections or single generic tag detection
        :rtype: list[GenericTagModel] or GenericTagModel
        """
        if tag_id is None:
            url = f"metadata/{asset_id}/generic_tags"
            response = Client.get(url)
        else:
            url = f"metadata/{asset_id}/generic_tags/{tag_id}"
            response = Client.get(url)

        if response is not None:
            if isinstance(response, dict):
                generic_tag = GenericTagModel(
                    id=response["id"],
                    name=response["name"],
                    time=response["time"],
                    score=response["score"],
                )
            elif isinstance(response, list):
                generic_tag = [GenericTagModel(**item) for item in response]

            return generic_tag
        else:
            return response
