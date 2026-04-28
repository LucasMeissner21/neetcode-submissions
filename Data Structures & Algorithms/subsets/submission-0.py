class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        window = [0] * n
        final = [1] * n

        while window != final:
            res.append([nums[i] for i in range(len(nums)) if window[i] == 1])
            i = 0
            while True:
                if window[i] == 1:
                    window[i] = 0
                    i += 1
                else:
                    window[i] = 1
                    break

        res.append(nums)
        return res