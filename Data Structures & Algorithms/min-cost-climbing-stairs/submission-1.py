class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Minimalistic, track the minimum cost of getting from each step to the top
        # starting from the top and working backwards to the starting 2 positions
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])