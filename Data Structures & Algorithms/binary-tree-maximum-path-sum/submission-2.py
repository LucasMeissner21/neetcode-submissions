# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Solution 1: Recursive DFS while updating max
        res = float("-inf")

        def dfs(root: Optional[TreeNode]) -> int:
            nonlocal res
            if not root:
                return 0

            left = max(dfs(root.left), 0) # Ignore negative paths
            right = max(dfs(root.right), 0) 

            res = max(left + right + root.val, res) # Update max path

            return max(left, right) + root.val # Return max left or right path until current

        dfs(root)
        return res
