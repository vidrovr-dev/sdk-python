# TODO: need to figure what to do, if anything, with this class

from abc import ABC, abstractmethod


class Resource(ABC):
    @abstractmethod
    def uri(cls, id):
        raise NotImplementedError

    @abstractmethod
    def get(cls, id):
        pass

    @abstractmethod
    def delete(cls, id):
        pass

    @abstractmethod
    def patch(cls, id):
        pass

    @abstractmethod
    def post(cls, id):
        pass
