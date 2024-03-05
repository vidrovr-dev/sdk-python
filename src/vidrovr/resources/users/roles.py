from src.vidrovr.core import Client

from pydantic import BaseModel


class RolesModel(BaseModel):
    """
    Model of role data

    :param id: ID of the role
    :type id: str
    :param name: Name of the role
    :type name: str
    :param description: Description of the role
    :type description: str
    """

    id: str = None
    name: str = None
    description: str = None


class Roles:
    @classmethod
    def read(cls):
        """
        Retrieve the available roles for a user.

        :return: A list of RolesModel objects
        :rtype: list[RolesModel]
        """
        url = f"users/roles"
        response = Client.get(url)

        if response is not None:
            roles = [RolesModel(**item) for item in response]

            return roles
        else:
            return response
