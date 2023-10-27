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
        """
        Retrieve information about an organization.

        :param org_id: ID of the organization
        :type org_id: str
        :return: Object with information about the organization
        :rtype: OrganizationData
        """
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
        """
        Update the name of an organization.
        
        :param org_id: ID of the organization
        :type org_id: str
        :param name: New name for the organization
        :type name: str
        :return: JSON string of the HTTP response
        :rtype: str
        """
        url      = f'organizations/{org_id}'
        payload  = {
            'data': {
                'name': name
            }
        }
        response = Client.patch(url, payload)

        return response