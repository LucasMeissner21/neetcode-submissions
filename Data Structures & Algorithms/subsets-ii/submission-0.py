class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Solution 1: Recurive function that gets every forward combination
        res = []
        current = []
        nums.sort()

        def getSubsets(start: int):
            res.append(current[:])
            for i in range(start, len(nums)): # Only allow looking forward
                if i > start and nums[i] == nums[i - 1]: # Skip duplicates
                    continue
                current.append(nums[i])
                getSubsets(i + 1) # Only allow looking forward, no repeats
                current.pop()
            return
        
        getSubsets(0)
        return res