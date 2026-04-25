class LRUCache:

    def __init__(self, capacity: int):
        # Attempt 1
        self.capacity = capacity # Int tracker for capacity
        self.recency = [] # stack to track recency
        self.cache = {} # cache data

    def get(self, key: int) -> int:
        if key in self.cache: # If key exists, update recency and return
            self.recency.remove(key)
            self.recency.append(key)
            return self.cache.get(key)
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache: # If key exists update recency and value
            self.cache[key] = value
            self.recency.remove(key)    
            self.recency.append(key)  
        else:
            self.cache[key] = value # Otherwise add key, value pair and update capacity
            self.recency.append(key)
            self.capacity -= 1
            if self.capacity < 0: # If over capacity, remove least recent and inc capacity
                remove = self.recency.pop(0)
                del self.cache[remove]
                self.capacity += 1
