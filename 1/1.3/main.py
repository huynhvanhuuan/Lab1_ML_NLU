from abc import ABC, abstractmethod


class Product(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def fromCountry(self):
        pass