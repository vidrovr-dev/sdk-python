from ...core import Client

from dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class CustomTagData:
    id: str
    name: str
    is_active: bool
    creation_date: str
    num_examples: int
    num_reviewed: int
    num_unreviewed: int

class CustomTag(BaseModel):

    @classmethod
    def read(cls, project_id: str, tag_id: str=None):
        if tag_id is None:
            url = f'customdata/tags/?project_uid={project_id}'
        else:
            url = f'customdata/tags/{tag_id}?project_uid={project_id}'

        response = Client.get(url)

        if isinstance(response, dict):
            custom_tag = CustomTagData(
                id=response['id'],
                name=response['name'],
                is_active=response['is_active'],
                creation_date=response['creation_date'],
                num_examples=response['num_examples'],
                num_reviewed=response['num_reviewed'],
                num_unreviewed=response['num_unreviewed']
            )
        elif isinstance(response, list): 
            custom_tag = [CustomTagData(**item) for item in response]

        return custom_tag
    
    @classmethod
    def delete(cls, tag_id: str, project_id: str):
        url      = f'customdata/tags/{tag_id}?project_uid={project_id}'
        response = Client.delete(url)

        return response
    
    @classmethod
    def create(cls, project_id: str, tag_name: str):
        url     = 'customdata/tags'
        payload = {
            'data': {
                'name': tag_name,
                'project_uid': project_id
            }
        }
        response = Client.post(url, payload)

        return response