class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Set index of corrosponding values as negative, if an index has already been set
        # negative, it means this is a duplicate
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] < 0:
                return index + 1
            nums[index] *= -1
        return -1

