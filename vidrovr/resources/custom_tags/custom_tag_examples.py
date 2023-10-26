from ...core import Client

from dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class CustomTagExampleData:
    id: str
    href: str
    source: str
    status: str

class CustomTagExample(BaseModel):

    @classmethod
    def read(cls, project_id: str, tag_id: str, example_id: str=None):
        if example_id is None:
            url = f'customdata/tags/{tag_id}/examples?project_uid={project_id}&status=&page_size=&page='
        else:
            url = f'customdata/tags/{tag_id}/examples/{example_id}?project_uid={project_id}'

        response = Client.get(url)

        if isinstance(response, dict):
            custom_tag = CustomTagExampleData(
                id=response['id'],
                href=response['href'],
                source=response['source'],
                status=response['status']
            )
        elif isinstance(response, list): 
            custom_tag = [CustomTagExampleData(**item) for item in response]

        return custom_tag
    
    @classmethod
    def update(cls, tag_id: str, example_id: str, project_id: str, new_label: str):
        url     = f'customdata/tags/{tag_id}/examples/{example_id}?project_uid={project_id}'
        payload = {
            'data': {
                'status': new_label,
                'project_uid': project_id
            }
        }
        response = Client.patch(url, payload)

        return response