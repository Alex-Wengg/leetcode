from sortedcontainers import SortedDict

class StockPrice:

    def __init__(self):
        self.latest_time = 0
        self.timestamp_price = {}
        self.price_frequency =SortedDict()

    def update(self, timestamp: int, price: int) -> None:
        
        self.latest_time = max(self.latest_time, timestamp)
        
        if timestamp in self.timestamp_price:
            oldPrice = self.timestamp_price[timestamp]
            
            self.price_frequency[oldPrice] -= 1
            if not self.price_frequency[oldPrice]:
                del self.price_frequency[oldPrice]
            
        self.timestamp_price[timestamp] = price
        
        if price in self.price_frequency:
            self.price_frequency[price] += 1
        else:
            self.price_frequency[price] = 1
            
    def current(self) -> int:
        return self.timestamp_price[self.latest_time]

    def maximum(self) -> int:
        return self.price_frequency.peekitem(-1)[0]

    def minimum(self) -> int:
        return self.price_frequency.peekitem(0)[0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()