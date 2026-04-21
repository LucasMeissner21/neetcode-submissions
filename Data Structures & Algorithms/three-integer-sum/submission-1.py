class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        # Sort so 2 pointer approach works
        nums.sort()
        # Enumerate so index and value can be tracked
        for i, a in enumerate(nums):
            # If a > 0 in sorted list, no more possible solutions
            if a > 0:
                break
            # If a is the same as previous value, skip
            if i > 0 and a == nums[i - 1]:
                continue
            # Set 2-pointer for remaining sum
            j = i + 1
            k = len(nums) - 1
            # 2 sum adjusted for 3rd sum and target of 0
            while j < k:
                target = nums[i] + nums[j] + nums[k]
                if target < 0:
                    j += 1
                elif target > 0:
                    k -= 1
                else:
                    res.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
            i += 1
        return res
                
