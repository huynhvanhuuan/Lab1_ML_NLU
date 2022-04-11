from datetime import date


class Product:
    def __init__(self, name: str, type: str, price: int, expiredDate: date):
        self.__name = name
        self.__type = type
        self.__price = price
        self.__expiredDate = expiredDate
