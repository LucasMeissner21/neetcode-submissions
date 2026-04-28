class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Solution 1: Backtracking using set to track if index is used in current
        res = []
        current = []
        used = set()

        def backtrack():
            if len(current) == len(nums): # Solution found
                res.append(current[:])
                return
            for i in range(len(nums)):
                if i in used: # If index is already in current, skip
                    continue
                used.add(i) # Track that current index is being used
                current.append(nums[i])
                backtrack()
                current.pop()
                used.remove(i)

        backtrack()
        return res