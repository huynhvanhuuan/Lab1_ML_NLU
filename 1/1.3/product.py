from datetime import date


class Product:
    def __init__(self, name: str, type: str, price: int, expiredDate: date):
        self.__name = name
        self.__type = type
        self.__price = price
        self.__expiredDate = expiredDate

    def getName(self):
        return self.__name

    def getType(self):
        return self.__type

    def getPrice(self):
        return self.__price

    def getExpiredDate(self):
        return self.__expiredDate
