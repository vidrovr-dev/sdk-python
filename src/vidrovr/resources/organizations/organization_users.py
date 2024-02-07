import json

from vidrovr.core import Client

from pydantic import BaseModel

class OrganizationUserModel(BaseModel):
    """
    Model of an organization user.

    :param id: ID of the user
    :type id: str
    :param email: Email of the user
    :type email: str
    :param role_id: ID of the role for the user
    :type role_id: str
    :param project_ids: List of project IDs the user is assigned to
    """
    id: str | None
    email: str | None
    role_id: str | None
    project_ids: list[str] | None

class OrganizationUser:

    @classmethod
    def read(cls, org_id: str):
        """
        Retrieve list of user IDs in an organization.
        
        :param org_id: ID of the organization
        :type org_id: str
        :return: Array of user IDs
        :rtype: list[OrganizationUserData]
        """
        url      = f'organizations/{org_id}/users/'
        response = Client.get(url)

        if response is not None:
            org_user = [OrganizationUserModel(**item) for item in response]

            return org_user
        else:
            return response
        
    @classmethod
    def update(cls, org_id: str, data: OrganizationUserModel):
        """
        Create a user in an organization.
        
        :param org_id: ID of the organization
        :type org_id: str
        :param data: Data object for the new user
        :type data: OrganizationNewUserData
        :return: JSON string of the HTTP response
        :rtype: str
        """
        url      = f'organizations/{org_id}/users/'
        payload  = {
            'data': {
                'email': data.email,
                'role_id': data.role_id,
                'project_ids': [data.project_ids]
            }
        }
        response = Client.patch(url, payload)

        if response is not None:
            user = OrganizationUserModel(
                id=response['id']
            )

            return user
        else:
            return response