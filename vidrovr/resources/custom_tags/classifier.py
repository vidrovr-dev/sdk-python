from ...core import Client

from dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class ClassifierData:
    id: str
    name: str
    training_state: str
    is_active: bool

class Classifier(BaseModel):

    @classmethod
    def read(cls, project_id: str, classifier_id: str=None):
        if classifier_id is None:
            url = f'customdata/classifiers/?project_uid={project_id}'
        else:
            url = f'customdata/classifiers/{classifier_id}?project_uid={project_id}'

        response = Client.get(url)

        if isinstance(response, dict):
            custom_tag = ClassifierData(
                id=response['id'],
                name=response['name'],
                training_state=response['training_state'],
                is_active=response['is_active']
            )
        elif isinstance(response, list): 
            custom_tag = [ClassifierData(**item) for item in response]

        return custom_tag
    
    @classmethod
    def create(cls, project_id: str):
        url     = f'customdata/classifiers'
        payload = {
            'data': {
                'project_uid': project_id
            }
        }
        response = Client.post(url, payload)

        return response 