class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.count = 0
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            self.count += 1
        else:
            self.cache.pop(key)
        self.cache[key] = value
        if self.count > self.capacity:
            self.cache.pop(next(iter(self.cache)))
            self.count -= 1
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)