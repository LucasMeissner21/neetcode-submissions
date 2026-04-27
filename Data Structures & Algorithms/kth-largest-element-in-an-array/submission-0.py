class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Min heap of max size k, scan nums and get k largest values then return root of 
        # heap
        heap = []

        for num in nums:
            heapq.heappush(heap, num)
            k -= 1
            if k < 0:
                heapq.heappop(heap)
                k += 1
        
        return heap[0]