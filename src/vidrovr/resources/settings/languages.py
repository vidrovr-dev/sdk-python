from src.vidrovr.core import Client

from pydantic import BaseModel


class LanguageModel(BaseModel):
    """
    Model of language settings.

    :param audio_input: Spoken language of the source in the format of ISO langauge code-ISO Region code (en-US)
    :type audio_input: str
    :param on_screen_input: Language of the text written on screen of the source in the format of ISO language code (en)
    :type on_screen_input: str
    :param output: Language of the transcript produced by the platform in the format of ISO language code (en)
    :type output: str
    """

    audio_input: str = None
    on_screen_input: str = None
    output: str = None


class Language(BaseModel):
    @classmethod
    def read(cls, project_id: str):
        """
        Retrieve information about the project language settings.

        :param project_id: ID of the project
        :type project_id: str
        :return: Data object containing information about the project language settings
        :rtype: LanguageData
        """
        url = f"settings/processing/{project_id}/languages"
        response = Client.get(url)

        if response is not None:
            language = LanguageModel(
                audio_input=response["audio_input"],
                on_screen_input=response["on_screen_input"],
                output=response["output"],
            )

            return language
        else:
            return response

    @classmethod
    def update(cls, project_id: str, data: LanguageModel):
        """
        Update the language settings for a project.

        :param project_id: ID of the project
        :type project_id: str
        :param data: Data object containing new language settings
        :type data: LanguageData
        :return: JSON string of the HTTP response
        :rtype: str
        """
        url = f"settings/processing/{project_id}/languages"
        payload = {"data": {}}

        if data.audio_input is not None:
            payload["data"]["audio_input"] = data.audio_input

        if data.on_screen_input is not None:
            payload["data"]["on_screen_input"] = data.on_screen_input

        if data.output is not None:
            payload["data"]["output"] = data.output

        response = Client.patch(url, payload)

        if response is not None:
            language = LanguageModel(
                audio_input=response["audio_input"],
                on_screen_input=response["on_screen_input"],
                output=response["output"],
            )

            return language
        else:
            return response
