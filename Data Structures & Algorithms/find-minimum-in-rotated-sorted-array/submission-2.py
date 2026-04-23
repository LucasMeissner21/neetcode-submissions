class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        while True:
            if nums[len(nums) - 1] > nums[0]:
                return nums[0]
            nums = nums[-1:] + nums[:-1]