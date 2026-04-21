class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {} # val : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in lookup:
                return [lookup[diff], i]
            lookup[n] = i
        return
