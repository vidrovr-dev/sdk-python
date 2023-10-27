from ...core import Client

from dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class LanguageData:
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
        url      = f'settings/processing/{project_id}/languages'
        response = Client.get(url)

        language = LanguageData(
            audio_input=response['audio_input'],
            on_screen_input=response['on_screen_input'],
            output=response['output']
        )

        return language
    
    @classmethod
    def update(cls, project_id: str, data: LanguageData):
        """
        Update the language settings for a project.
        
        :param project_id: ID of the project
        :type project_id: str
        :param data: Data object containing new language settings
        :type data: LanguageData
        :return: JSON string of the HTTP response
        :rtype: str
        """
        url     = f'settings/processing/{project_id}/languages'
        payload = {
            'data': { }
        }

        if data.audio_input is not None:
            payload['data']['audio_input'] = data.audio_input

        if data.on_screen_input is not None:
            payload['data']['on_screen_input'] = data.on_screen_input

        if data.output is not None:
            payload['data']['output'] = data.output

        response = Client.patch(url, payload)

        return response