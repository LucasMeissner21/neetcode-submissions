class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Solution 1: use a binary window to get all subsets
        res = []
        n = len(nums)

        # Establish window for binary and final for end state
        window = [0] * n
        final = [1] * n

        # Loops until all states have been added to res
        while window != final:
            # Only add nums where binary is matched
            res.append([nums[i] for i in range(len(nums)) if window[i] == 1])
            i = 0
            # Binary inc by 1
            while True:
                if window[i] == 1:
                    window[i] = 0
                    i += 1
                else:
                    window[i] = 1
                    break
        # Add entire nums list to res
        res.append(nums)
        return res