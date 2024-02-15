from src.vidrovr.core import Client

from pydantic import BaseModel


class IABTagModel(BaseModel):
    """
    Model of an IAB tag

    :param id: ID of the detection
    :type id: str
    :param name: Name of the IAB tag detected
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


class IABTag:
    @classmethod
    def read(cls, asset_id: str, tag_id: str = None):
        """
        Returns an array of IAB tag detections or information about a specific IAB tag detection.

        :param asset_id: ID of the asset
        :type asset_id: str
        :param tag_id: ID of the tag or None
        :type tag_id: str
        :return: Array of IAB tag detections or single IAB tag detection
        :rtype: list[IABTagModel] or IABTagModel
        """
        if tag_id is None:
            url = f"metadata/{asset_id}/iab_tags"
            response = Client.get(url)
        else:
            url = f"metadata/{asset_id}/iab_tags/{tag_id}"
            response = Client.get(url)

        if response is not None:
            if isinstance(response, dict):
                iab_tag = IABTagModel(
                    asset_id=response["id"],
                    name=response["name"],
                    time=response["time"],
                    score=response["score"],
                )
            elif isinstance(response, list):
                iab_tag = [IABTagModel(**item) for item in response]

            return iab_tag
        else:
            return response
