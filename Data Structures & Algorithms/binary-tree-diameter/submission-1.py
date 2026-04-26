# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Recursive solution (dfs) using global result tracker
        res = 0

        def dfs(root: Optional[TreeNode]) -> int:
            nonlocal res # uses res from one scope outside

            if not root: # Basecase
                return 0

            # Recursive call to get left tree length and right tree length
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left + right) # Update max diameter

            return 1 + max(left, right) # Return max height from current node to leaf

        # Call recursive function and return result
        dfs(root)
        return res