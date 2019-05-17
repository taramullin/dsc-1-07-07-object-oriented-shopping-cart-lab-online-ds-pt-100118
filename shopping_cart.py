class ShoppingCart():
    def __init__(self, _total=0, _items=[], _employee_discount=None):
        self._total = sum([i['price']*i['quantity'] for i in _items])
        self._items = _items
        self._employee_discount = _employee_discount
    def add_item(self, name, price, quantity=1):
        for i in list(range(quantity)):
            self._items.append({'name': name, 'price': price})
            self._total += price
        return self._total

    def mean_item_price(self):
        num_items = len(self._items)
        total = self._total
        mean = total/num_items
        return mean

    def median_item_price(self):
        prices = [item['price'] for item in self._items]
        length = len(prices)
        if (length%2 == 0):
            mid_one = int(length/2)
            mid_two = mid_one - 1
            median = (price[mid_one] + prices[mid_two])/2
            return median
        mid = int(length/2)
        return prices[mid]

    def apply_discount(self):
        if self._employee_discount:
            discount = self._employee_discount/100
            disc_total = self._total * (1 - discount)
            return disc_total
        else:
            return "Sorry, there is no discount to apply to your cart :("

    def void_last_item(self):
        if self._items:
            removed_item = self._items.pop()
        else:
            return "There are no items in your cart!"
        self._total -= removed_item['price']
