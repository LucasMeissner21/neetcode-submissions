class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list) # Hashmap to store key = key, val = (val, timestamp)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        states = self.timemap[key]
        if states == None: # Base case, trying to get an unset value
            return ""
        l = 0
        r = len(states) - 1
        closest = ""

        while l <= r: # Binary search for closest to timestamp (<=)
            mid = (l + r) // 2
            
            if states[mid][1] == timestamp:
                return states[mid][0]
            
            if states[mid][1] > timestamp: # If mid is greater than timestamp, no need to update closest
                r = mid - 1
            else:
                closest = states[mid][0] # If mid is less than timestamp, it is the new closest
                l = mid + 1
        
        return closest
