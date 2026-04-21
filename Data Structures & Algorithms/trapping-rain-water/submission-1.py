class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        # Get prefix maxes
        prefix = [0] * n
        prefix[0] = height[0]
        for i in range(1, n):
            prefix[i] = max(prefix[i-1], height[i])
        # Get suffix maxes
        suffix = [0] * n
        suffix[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            suffix[i] = max(suffix[i+1], height[i])
        # Determine trapped water based on prefixes and suffixes
        res = 0
        for i in range(len(height)):
            res += min(prefix[i], suffix[i]) - height[i]
        return res