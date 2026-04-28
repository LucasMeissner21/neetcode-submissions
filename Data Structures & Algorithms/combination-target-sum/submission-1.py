class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Solution 1: Recurive function that gets every forward combination
        res = []
        current = []

        def getToTarget(start: int, target: int):
            if target == 0: # Target hit, add to res
                res.append(current[:])
                return
            if target < 0: # Target missed, return
                return
            for i in range(start, len(nums)): # Only allow looking forward
                current.append(nums[i])
                getToTarget(i, target - nums[i]) # Only allow looking forward
                current.pop()
            return
        
        getToTarget(0, target)
        return res
