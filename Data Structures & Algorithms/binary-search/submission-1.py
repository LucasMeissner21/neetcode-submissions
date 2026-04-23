class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid = int(len(nums) / 2)
        if target == nums[mid]:
            return mid

        if len(nums) == 1:
            return -1

        if target > nums[mid]:
            ind = self.search(nums[mid:], target)
            return mid + ind if ind != -1 else -1
            
        if target < nums[mid]:
            ind = self.search(nums[:mid], target)
            return ind if ind != -1 else -1
