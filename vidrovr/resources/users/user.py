from ...core import Client

from dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class UserData:
    asset_id: str
    email: str
    auth0_id: str
    organization_id: str
    creation_date: str
    role_name: str
    role_id: str

class User(BaseModel):

    @classmethod
    def read(cls, user_id: str):
        """
        Retrieve information about a specific user.

        :param user_id: ID of the user
        :type user_id: str
        :return: Data object containing information about the user
        :rtype: UserData
        """
        url      = f'users/{user_id}'
        response = Client.get(url)

        user = UserData(
            asset_id=response['id'],
            email=response['email'],
            auth0_id=response['auth0_id'],
            organization_id=response['organization_id'],
            organization_creation_date=response['creation_date'],
            role_name=response['role_name'],
            role_id=response['role_id']
        )

        return user
    
    @classmethod
    def delete(cls, user_id: str): 
        """
        Delete a specific user.
        
        :param user_id: ID of the user
        :type user_id: str
        :return: JSON string of the HTTP response
        :rtype: str
        """
        url      = f'users/{user_id}'
        response = Client.delete(url)

        return response
    
    @classmethod
    def update(cls, user_id: str, data: UserData):
        """
        Update information about a user.
        
        :param user_id: ID of the user
        :type user_id: str
        :param data: Data object containing update information
        :type data: UserData
        :return: JSON string of the HTTP response
        :rtype: str
        """
        url      = f'users/{user_id}'
        payload  = {
            'data': {
                'name': data.email,
                'role_id': data.role_id
            }
        }
        response = Client.patch(url, payload)

        return response
