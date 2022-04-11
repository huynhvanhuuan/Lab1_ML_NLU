from datetime import date
from orderItem import OrderItem


class Order:
    id: str
    customer: str
    employee: str
    date: date
    items: list[OrderItem]

    def __init__(self):
        pass
