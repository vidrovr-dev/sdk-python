from vidrovr.core import Client

from pydantic import BaseModel

class OrganizationModel(BaseModel):
    """
    Model of an organization

    :param id: ID of the organization
    :type id: str
    :param organization_name: Name of the organization
    :type organization_name: str
    :param organization_status: Status of the organization
    :type organization_status: str
    """
    id: str
    organization_name: str
    organization_status: str

class Organization:

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
        
        if response is not None:
            org = OrganizationModel(
                id=response['id'],
                organization_name=response['organization_name'],
                organization_status=response['organization_status']
            )

            return org
        else:
            return response
    
    @classmethod
    def update(cls, data: OrganizationModel):
        """
        Update the name of an organization.
        
        :param org_id: ID of the organization
        :type org_id: str
        :param name: New name for the organization
        :type name: str
        :return: JSON string of the HTTP response
        :rtype: str
        """
        url      = f'organizations/{data.id}'
        payload  = {
            'data': {
                'name': data.organization_name
            }
        }
        response = Client.patch(url, payload)

        if response is not None:
            org = OrganizationModel(
                id=response['id']
            )

            return org
        else:
            return response