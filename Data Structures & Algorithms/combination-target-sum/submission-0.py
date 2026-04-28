class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Solution 1: Recurive function
        res = []
        current = []

        def getToTarget(start: int, target: int):
            if target == 0:
                res.append(current[:])
                return
            if target < 0:
                return
            for i in range(start, len(nums)):
                current.append(nums[i])
                getToTarget(i, target - nums[i])
                current.pop()
            return
        
        getToTarget(0, target)
        return res
