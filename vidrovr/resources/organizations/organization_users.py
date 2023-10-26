import json

from ...core import Client

from dataclasses import dataclass
from pydantic import BaseModel
from icecream import ic

@dataclass
class OrganizationUserData:
    id: str

@dataclass
class OrganizationNewUserData:
    email: str
    role_id: str
    project_ids: str

class OrganizationUser(BaseModel):

    @classmethod
    def read(cls, org_id: str):
        url      = f'organizations/{org_id}/users/'
        response = Client.get(url)
        org_user = [OrganizationUserData(**item) for item in response]

        return org_user
    
    @classmethod
    def update(cls, org_id: str, data: OrganizationNewUserData):
        url      = f'organizations/{org_id}/users/'
        payload  = {
            'data': {
                'email': data.email,
                'role_id': data.role_id,
                'project_ids': [data.project_ids]
            }
        }
        response = Client.patch(url, payload)

        return response