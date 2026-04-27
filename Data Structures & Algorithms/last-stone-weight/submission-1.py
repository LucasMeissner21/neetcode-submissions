class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Implement max-heap and pop 2 largest elements, abs their subtraction,
        # if non-zero, push back to heap
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            smash1 = -1 * heapq.heappop(stones)
            smash2 = -1 * heapq.heappop(stones)

            smash1 = smash1 - smash2
            if smash1 > 0:
                heapq.heappush(stones, -1 * smash1)

        return -1 * stones[0] if stones else 0