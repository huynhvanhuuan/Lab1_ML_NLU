from product import Product


class OrderItem:
    def __init__(self, item: Product, amount: int):
        self.__item = item
        self.__amount = amount
