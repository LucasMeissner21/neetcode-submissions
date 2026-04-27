class MedianFinder:

    def __init__(self):
        # Heaps where median will be at top
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        # if number greater than minheap's minimum, add to minheap
        if self.minHeap and num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        # otherwise, add to maxheap, this splits all less than median values on maxheap
        # and all greater than median values on minheap
        else:
            heapq.heappush(self.maxHeap, -1 * num)

        # Balance the heaps if unbalanced
        if len(self.maxHeap) > len(self.minHeap) + 1:
            val = -1 * heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > len(self.maxHeap) + 1:
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -1 * val)

    def findMedian(self) -> float:
        # Return the top element from the longer list
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        elif len(self.maxHeap) > len(self.minHeap):
            return -1 * self.maxHeap[0]
        # or the average of the 2 if balanced
        else:
            return (-1 * self.maxHeap[0] + self.minHeap[0]) / 2

        