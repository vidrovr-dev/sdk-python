from src.vidrovr.core import Client

from pydantic import BaseModel


class UserModel(BaseModel):
    """
    Model of a user

    :param id: ID of the user
    :type id: str
    :param email: Email address of the user
    :type email: str
    :param auth0_id: Auth0 ID for the user
    :type auth0_id: str
    :param organization_id: ID of the organization the user belongs to
    :type organization_id: str
    :param creation_date: Creation date of the user
    :type creation_date: str
    :param role_name: Name of the role the user has been assigned
    :type role_name: str
    :param role_id: ID of the role the user has been assigned
    :type role_id: str
    """

    id: str = None
    email: str = None
    auth0_id: str = None
    organization_id: str = None
    creation_date: str = None
    role_name: str = None
    role_id: str = None


class User:
    @classmethod
    def read(cls, user_id: str):
        """
        Retrieve information about a specific user.

        :param user_id: ID of the user
        :type user_id: str
        :return: Data object containing information about the user
        :rtype: UserModel
        """
        url = f"users/{user_id}"
        response = Client.get(url)

        if response is not None:
            user = UserModel(
                id=response["id"],
                email=response["email"],
                auth0_id=response["auth0_id"],
                organization_id=response["organization_id"],
                organization_creation_date=response["creation_date"],
                role_name=response["role_name"],
                role_id=response["role_id"],
            )

            return user
        else:
            return response

    @classmethod
    def delete(cls, user_id: str):
        """
        Delete a specific user.

        :param user_id: ID of the user
        :type user_id: str
        :return: Data object of the user model
        :rtype: UserModel
        """
        url = f"users/{user_id}"
        response = Client.delete(url)

        if response is not None:
            user = UserModel(id=response["id"])

            return user
        else:
            return response

    @classmethod
    def update(cls, user_id: str, data: UserModel):
        """
        Update information about a user.

        :param user_id: ID of the user
        :type user_id: str
        :param data: Data object containing update information
        :type data: UserData
        :return: Data object of the user model
        :rtype: UserModel
        """
        url = f"users/{user_id}"
        payload = {"data": {"name": data.email, "role_id": data.role_id}}
        response = Client.patch(url, payload)

        if response is not None:
            user = UserModel(id=response["id"])

            return user
        else:
            return response
