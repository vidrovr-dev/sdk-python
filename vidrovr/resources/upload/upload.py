from ...core import Client

from dataclasses import dataclass
from pydantic import BaseModel

class Upload(BaseModel):

    @classmethod
    def read(cls):
        pass