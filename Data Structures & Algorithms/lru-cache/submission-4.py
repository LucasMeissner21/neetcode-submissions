class LRUCache:

    def __init__(self, capacity: int):
        # Attempt 2: Optimize space with OrderedDict
        self.capacity = capacity # Int tracker for capacity
        self.cache = OrderedDict() # ordered cache data

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache: # If key exists update recency and value
            self.cache.move_to_end(key) 
        else:
            self.capacity -= 1
        self.cache[key] = value
        if self.capacity < 0:
            self.cache.popitem(last=False)
            self.capacity += 1
