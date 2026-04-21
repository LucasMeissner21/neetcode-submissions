class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]
        for i in range(1, len(nums)):
            new = nums[0] * res[0]
            res = [r * nums[i] for r in res]
            res.append(new)
        return res