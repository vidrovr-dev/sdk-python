from src.vidrovr.core import Client

from pydantic import BaseModel


class TranscriptModel(BaseModel):
    """
    Model of transcript detection

    :param id: ID of the detection
    :type id: str
    :param text: Text in the transcript chunk
    :type text: str
    :param start_time: Timestamp for the start of the transcript chunk
    :type start_time: str
    :param end_time: Timestamp for the end of the transcript chunk
    :type end_time: str
    :param duration: Length of the transcript chunk
    :type duration: float
    :param language_id: ID of the transcript language
    :type language_id: str
    :param language_name: Name of the transcript language
    :type language_name: str
    :param language_slug: ISO language code of the transcript language
    :type language_slu: str
    """

    id: str = None
    text: str = None
    start_time: str = None
    end_time: str = None
    duration: float = 0.0
    language_id: str = None
    language_name: str = None
    language_slug: str = None


class Transcript:
    @classmethod
    def read(cls, asset_id: str, transcript_id: str):
        """
        Returns detail information for a specific transcript chunk.

        :param asset_id: ID of the asset
        :type asset_id: str
        :param transcript_id: ID of the transcript
        :type transcript_id: str
        :return: Data object containing transcript information
        :rtype: TranscriptData
        """
        url = f"metadata/{asset_id}/transcripts/{transcript_id}"
        response = Client.get(url)

        if response is not None:
            transcript = TranscriptModel(
                id=response["id"],
                text=response["text"],
                start_time=response["start_time"],
                end_time=response["end_time"],
                duration=response["duration"],
                language_id=response["language_id"],
                language_name=response["language_name"],
                language_slug=response["language_slug"],
            )

            return transcript
        else:
            return response
