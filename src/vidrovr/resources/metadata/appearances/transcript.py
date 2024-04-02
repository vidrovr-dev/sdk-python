from vidrovr.core import Client

from pydantic import BaseModel


class TranscriptAppearancesModel(BaseModel):
    """
    Model of person appearances

    :param id: ID of the transcript appearance
    :type id: str
    :param language: Language of the transcript appearing
    :type language: str
    :param text: Text of the transcript appearance
    :type text: str
    :param start: Timestamp for the start of the transcript appearance
    :type start: str
    :param end: Timestamp for the end of the transcript appearance
    :type end: str
    """

    id: str = None
    language: str = None
    text: str = None
    start: str = None
    end: str = None


class TranscriptAppearances:
    @classmethod
    def read(cls, asset_id: str):
        """
        Returns an array of transcript chunks for the asset.

        :param asset_id: ID of the asset
        :type asset_id: str
        :return: Array of information about the transcript chunks
        :rtype: list[TranscriptAppearanceModel]
        """
        url = f"metadata/{asset_id}/appearances/transcripts"
        response = Client.get(url)
        transcript = [TranscriptAppearancesModel(**item) for item in response]

        return transcript
