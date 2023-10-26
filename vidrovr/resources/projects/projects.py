from ...core import Client

from dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class ProjectData:
    id: str
    name: str
    user_ids: str
    creation_date: str

@dataclass
class ProjectList:
    id: str
    name: str

class Project(BaseModel):

    @classmethod
    def read(cls, project_id: str = None):
        if project_id is None:
            url = f'projects/'
        else:
            url = f'projects/{project_id}'

        response = Client.get(url)

        if isinstance(response, dict):
            project = ProjectData(
                id=response['id'],
                name=response['name'],
                user_ids=response['user_ids'],
                creation_date=response['creation_date']
            )
        elif isinstance(response, list):
            project = [ProjectList(**item) for item in response]

        return project
    
    @classmethod
    def delete(cls, project_id: str):
        url      = f'projects/{project_id}'
        response = Client.delete(url)

        return response
    
    @classmethod
    def update(cls, project_id: str, user_id: str, name: str, operation: str):
        url      = f'projects/{project_id}'
        payload  = {
            'data': {
                'name': name,
                'operation': operation, # 'add' or 'remove'
                'user_ids': [user_id]
            }
        }
        response = Client.patch(url, payload)

        return response
    
    @classmethod
    def create(cls, user_id: str, name: str):
        url      = f'projects/'
        payload  = {
            'data': {
                'name': name,
                'user_ids': [user_id]
            }
        }
        response = Client.post(url, data=payload)

        return response