class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Modified bucket sort
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        # Count how many times each number occurs
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # Update frequency array for each key, value pair in count
        for n, c in count.items():
            freq[c].append(n)

        # Get k most occuring
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
            if len(res) == k:
                return res
        return