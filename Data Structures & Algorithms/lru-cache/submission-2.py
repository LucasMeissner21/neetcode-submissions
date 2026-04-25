class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.recency = []
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            self.recency.remove(key)
            self.recency.append(key)
            return self.cache.get(key)
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.recency.remove(key)    
            self.recency.append(key)  
        else:
            self.cache[key] = value
            self.recency.append(key)
            self.capacity -= 1
            if self.capacity < 0:
                remove = self.recency.pop(0)
                del self.cache[remove]
                self.capacity += 1
