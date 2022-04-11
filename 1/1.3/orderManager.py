from order import Order


class OrderManager:
    orders: list[Order]

    def __init__(self):
        pass

    def highest_price(self):
        highestPrice = 0
        for order in self.orders:
            for orderItem in order.items:
                price = orderItem.getItem().getPrice()
                if price > highestPrice:
                    highestPrice = price
        return highestPrice

    def statistics(self):
        d = {}
        for order in self.orders:
            for orderItem in order.items:
                item = orderItem.getItem()
                if item.getType() in d:
                    d[item.getType()] += 1
                else:
                    d[item.getType()] = 1
        return d

    
