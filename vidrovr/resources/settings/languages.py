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