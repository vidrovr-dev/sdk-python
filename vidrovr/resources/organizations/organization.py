from ...core import Client

from dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class OrganizationData:
    id: str
    organization_name: str
    organization_status: str

class Organization(BaseModel):

    @classmethod
    def read(cls, org_id: str):
        url      = f'organizations/{org_id}'
        response = Client.get(url)

        user = OrganizationData(
            id=response['id'],
            organization_name=response['organization_name'],
            organization_status=response['organization_status']
        )

        return user
    
    @classmethod
    def update(cls, org_id: str, name: str):
        url      = f'organizations/{org_id}'
        payload  = {
            'data': {
                'name': name
            }
        }
        response = Client.patch(url, payload)

        return response