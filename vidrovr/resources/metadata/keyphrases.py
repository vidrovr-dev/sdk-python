from ...core import Client

from dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class KeyphraseData:
    id: str
    keyphrase: str
    confidence: float

class Keyphrase(BaseModel):

    @classmethod
    def read(cls, asset_id: str):
        """
        Returns an array of keyphrase detections for the asset.

        :param asset_id: ID of the asset
        :type asset_id: str
        :return: Array of keyphrase detections
        :rtype: list[KeyphraseData]
        """
        url       = f'metadata/{asset_id}/keyphrases'
        response  = Client.get(url)
        keyphrase = [KeyphraseData(**item) for item in response]

        #keyphrase = KeyphraseData(
        #    asset_id=response['id'],
        #    keyprhase=response['keyphrase'],
        #    confidence=response['confidence'],
        #)

        return keyphrase