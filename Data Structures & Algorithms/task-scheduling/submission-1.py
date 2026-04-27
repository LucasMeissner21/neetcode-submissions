class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Solution 1: Get frequency of all tasks, put into maxheap, then use queue with 
        # wait time to hold off on cooldown tasks

        freq = {} # Stores initial frequency
        maxHeap = [] # Stores tasks and frequency by descending frequency
        queue = [] # FIFO

        # Initialize frequency hashmap
        for task in tasks:
            count = freq.get(task, 0)
            freq[task] = count + 1

        # Add all tasks to maxheap descending by count
        for task, count in freq.items():
            heapq.heappush(maxHeap, [ -1 * count, task])

        # Calculate cpu cycles
        cycles = 0
        while maxHeap or queue:
            cycles += 1
            if queue and queue[0][2] == cycles:
                count, task, cd = queue.pop(0)
                heapq.heappush(maxHeap, [-1 * count, task])
            if maxHeap:
                count, task = heapq.heappop(maxHeap)
                count = -1 * count
                count -= 1
                if count > 0:
                    queue.append([count, task, cycles + n + 1])
            
        return cycles