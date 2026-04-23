class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Binary search, base adjusted l and r off whether a side is sorted
        # If side is sorted, and target is in that side, adjust accordingly

        l = 0
        r = len(nums) - 1

        while l <= r:
            if nums[l] == target: # Check if boundary is target
                return l
            if nums[r] == target:
                return r
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]: # Left side sorted
                if nums[l] < target and nums[mid] > target: # Target in left
                    r = mid - 1
                else:
                    l = mid + 1
            else: # Right side sorted
                if nums[r] > target and nums[mid] < target: # Target in right
                    l = mid + 1
                else:
                    r = mid - 1

        return -1