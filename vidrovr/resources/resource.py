# TODO: need to figure what to do, if anything, with this class

from abc import ABC

class Resource(ABC):
    def uri(cls, id):
        raise NotImplementedError
    
    def get(cls, id):
        pass

    def delete(cls, id):
        pass

    def patch(cls, id):
        pass

    def post(cls, id):
        pass