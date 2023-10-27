from ...core import Client

from dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class RolesData:
    id: str
    name: str
    description: str

class Roles(BaseModel):

    @classmethod
    def read(cls):
        """
        Retrieve the available roles for a user.
        
        :return: Array of roles
        :rtype: list[RolesData]
        """
        url      = f'users/roles'
        response = Client.get(url)
        roles    = [RolesData(**item) for item in response]

        return roles