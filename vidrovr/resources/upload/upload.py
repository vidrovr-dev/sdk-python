from vidrovr.core import Client

from pydantic import BaseModel

class Upload(BaseModel):

    @classmethod
    def read(cls):
        pass