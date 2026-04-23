class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Combine matrix into single list then perform iterative binary search
        vals = []

        for i in range(len(matrix)):
            vals += matrix[i]

        l = 0
        r = len(vals) - 1

        while l <= r:
            mid = int((l + r) / 2)

            if vals[mid] < target:
                l = mid + 1
            
            elif vals[mid] > target:
                r = mid - 1

            else:
                return True
        return False