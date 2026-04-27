class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k_dec = k # Tracks how many elements in heap relative to k
        self.heap = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        self.k_dec -= 1
        if self.k_dec < 0:
            heapq.heappop(self.heap)
            self.k_dec += 1
        return self.heap[0]