class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for val in nums:
            if val in hashset:
                return True
            else:
                hashset.add(val)
        return False
