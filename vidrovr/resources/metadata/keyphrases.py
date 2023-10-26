from ...core import Client

from dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class KeyphraseData:
    asset_id: str
    keyphrase: str
    confidence: float

class Keyphrase(BaseModel):

    @classmethod
    def read(cls, asset_id: str):
        url      = f'metadata/{asset_id}/keyphrases'
        response = Client.get(url)

        keyphrase = KeyphraseData(
            asset_id=response['id'],
            keyprhase=response['keyphrase'],
            confidence=response['confidence'],
        )

        return keyphrase