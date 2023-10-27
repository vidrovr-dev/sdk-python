from ....core import Client

from dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class TranscriptAppearanceData:
    id: str
    language: str
    text: str
    start: str
    end: str

class TranscriptAppearances(BaseModel):

    @classmethod
    def read(cls, asset_id: str):
        """
        Returns an array of transcript chunks for the asset.

        :param asset_id: ID of the asset
        :type asset_id: str
        :return: Array of information about the transcript chunks
        :rtype: list[TranscriptAppearanceData]
        """
        url        = f'metadata/{asset_id}/appearances/transcripts'
        response   = Client.get(url)
        transcript = [TranscriptAppearanceData(**item) for item in response]

        return transcript