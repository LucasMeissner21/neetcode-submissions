class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k_dec = k # Tracks how many elements in heap relative to k
        self.heap = [] # Heap of k largest elements
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val) # Add new value to heap
        self.k_dec -= 1 # update how many values needed for heap to be full
        if self.k_dec < 0: # If heap exceeds size, remove smallest value, inc k_dec
            heapq.heappop(self.heap)
            self.k_dec += 1
        return self.heap[0] # Return new smallest value