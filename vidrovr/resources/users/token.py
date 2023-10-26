from ...core import Client

from dataclasses import dataclass
from pydantic import BaseModel
from icecream import ic

@dataclass
class TokenData:
    id: str
    name: str
    creation_date: str
    is_active: bool

class Token(BaseModel):

    @classmethod
    def read(cls, user_id: str):
        url      = f'users/{user_id}/tokens'
        response = Client.get(url)

        if isinstance(response, dict):
            token_object = TokenData(
                id=response['id'],
                name=response['name'],
                creation_date=response['creation_date'],
                is_active=response['is_active']
            )
        elif isinstance(response, list):
            token_object = [TokenData(**item) for item in response]

        return token_object
    
    @classmethod
    def create(cls, user_id: str):
        url      = f'users/{user_id}/tokens'
        response = Client.post(url)

        token = TokenData(
            asset_id=response['id']
        )

        return token
