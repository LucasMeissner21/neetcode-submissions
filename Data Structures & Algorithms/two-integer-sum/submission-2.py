class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {} # val : index

        # Iterate through nums, enumerate into [index (i), number (n)]
        for i, n in enumerate(nums):
            # Get difference between current and target values
            diff = target - n
            # If difference value previously found, return solution
            if diff in lookup:
                return [lookup[diff], i]
            # Otherwise update lookup (hashmap)
            lookup[n] = i
        return
