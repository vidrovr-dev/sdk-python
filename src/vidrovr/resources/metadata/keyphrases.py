from vidrovr.core import Client

from pydantic import BaseModel

class KeyphraseModel(BaseModel):
    """
    Model of a keyphrase

    :param id: ID of the keyphrase
    :type id: str
    :param keyphrase: The keyphrase detected
    :type keyphrase: str
    :param confidence: Confidence score of the detection
    :type confidence: float
    """
    id: str = None
    keyphrase: str = None
    confidence: float = 0.0

class Keyphrase:

    @classmethod
    def read(cls, asset_id: str):
        """
        Returns an array of keyphrase detections for the asset.

        :param asset_id: ID of the asset
        :type asset_id: str
        :return: Array of keyphrase detections
        :rtype: list[KeyphraseModel]
        """
        url       = f'metadata/{asset_id}/keyphrases'
        response  = Client.get(url)

        if response is not None:
            keyphrase = [KeyphraseModel(**item) for item in response]

            #keyphrase = KeyphraseData(
            #    asset_id=response['id'],
            #    keyprhase=response['keyphrase'],
            #    confidence=response['confidence'],
            #)

            return keyphrase
        else:
            return response