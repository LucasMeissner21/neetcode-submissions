class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hm = defaultdict(int)
        res = 0

        for n in nums:
            if not hm[n]:
                hm[n] = hm[n-1] + hm[n+1] + 1
                hm[n - hm[n-1]] = hm[n]
                hm[n + hm[n+1]] = hm[n]
                res = max(res, hm[n])

        return res
