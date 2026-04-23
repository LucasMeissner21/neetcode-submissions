class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Recursive binary search, check midpoint for target, otherwise recursive call the half the target should be in
        # Base case: if only 1 element in array and it is not target, return -1
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
