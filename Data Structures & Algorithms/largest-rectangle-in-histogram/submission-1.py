class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Create a stack with indexes and heights, parse through heights list. While smaller index is next, pop off values and compute
        # area they extended to the right. Add new small value, but set its index to be the furthest left that was popped off (greater)
        # so when it is calculated, it includes expansion leftwards
        maxArea = 0
        stack = [] # index, height
        
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append([start, h])
        
        # Clean up values that extended all the way to the right
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea
                    