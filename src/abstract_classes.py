from abc import ABC, abstractmethod


class Prod(ABC):

    @property
    @abstractmethod
    def price(self):
        pass

    @price.setter
    @abstractmethod
    def price(self, value):
        pass
