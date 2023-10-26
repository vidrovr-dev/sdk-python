from ...core import Client

from dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class TranscriptData:
    asset_id: str
    text: str
    start_time: str
    end_time: str
    duration: float
    language_id: str
    language_name: str
    language_slug: str

class Transcript(BaseModel):

    @classmethod
    def read(cls, asset_id: str, transcript_id: str):
        url      = f'metadata/{asset_id}/transcripts/{transcript_id}'
        response = Client.get(url)

        transcript = TranscriptData(
            asset_id=response['id'],
            text=response['text'],
            start_time=response['start_time'],
            end_time=response['end_time'],
            duration=response['duration'],
            language_id=response['language_id'],
            language_name=response['language_name'],
            language_slug=response['language_slug']
        )

        return transcript