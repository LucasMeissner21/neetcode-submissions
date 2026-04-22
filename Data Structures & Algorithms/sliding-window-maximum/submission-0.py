class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        # Initialize left/right max array to track k length window max values from left and right
        leftMax = [0] * n
        rightMax = [0] * n

        # Set first value
        leftMax[0] = nums[0]
        rightMax[n-1] = nums[n-1]

        for i in range(1, n):
            # For left window
            # If i % k, previous max value may not be valid, reset, otherwise adjust max at index
            if i % k == 0:
                leftMax[i] = nums[i]
            else:
                leftMax[i] = max(leftMax[i - 1], nums[i])

            # For right window
            # If n - 1 - i % k, previous max value may not be valid, reset, otherwise adjust max at index
            if (n - 1 - i) % k == 0:
                rightMax[n - 1 - i] = nums[n - 1 - i]
            else:
                rightMax[n - 1 - i] = max(rightMax[n - i], nums[n - 1 - i])
        
        # Set result array to number of k sized windows in nums
        res = [0] * (n - k + 1)

        # Result for each window is max of rightmost leftmax and leftmost right max
        for i in range(n - k + 1):
            res[i] = max(leftMax[i + k - 1], rightMax[i])

        return res
