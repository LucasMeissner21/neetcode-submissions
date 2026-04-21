class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Allows for quick lookup of values in O(1) avg. Lookup time and O(1) Insert time, with O(n) space comp
        hashset = set()
        # Iterate through list, if value in the set, return true, otherwise add to set and continue
        for val in nums:
            if val in hashset:
                return True
            else:
                hashset.add(val)
        # False if duplicate not found
        return False
