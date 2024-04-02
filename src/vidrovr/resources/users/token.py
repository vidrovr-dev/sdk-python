from vidrovr.core import Client

from pydantic import BaseModel


class TokenModel(BaseModel):
    """
    Model of token data

    :param id: ID of the token
    :type id: str
    :param name: Name of the token
    :type id: str
    :param creation_date: Creation date for the token
    :type creation_date: str
    :param is_active: Indicates if the token is active or not
    :type is_active: bool
    """

    id: str = None
    name: str = None
    creation_date: str = None
    is_active: bool = False


class Token:
    @classmethod
    def read(cls, user_id: str):
        """
        Retrieve information about a user's tokens.

        :param user_id: ID of the user
        :type user_id: str
        :return: Array of token information
        :rtype: list[TokenData]
        """
        url = f"users/{user_id}/tokens"
        response = Client.get(url)

        if response is not None:
            if isinstance(response, dict):
                token = TokenModel(
                    id=response["id"],
                    name=response["name"],
                    creation_date=response["creation_date"],
                    is_active=response["is_active"],
                )
            elif isinstance(response, list):
                token = [TokenModel(**item) for item in response]

            return token
        else:
            return response

    @classmethod
    def create(cls, user_id: str):
        """
        Create a new token for a user.

        :param user_id: ID of the user
        :type user_id: str
        :return: Data object containing new token ID
        :rtype: TokenModel
        """
        url = f"users/{user_id}/tokens"
        response = Client.post(url)

        if response is not None:
            token = TokenModel(asset_id=response["id"])

            return token
        else:
            return response
