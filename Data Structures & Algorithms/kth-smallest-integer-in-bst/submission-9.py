# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Solution 2: Recursive DFS with global count and res, still traversing smallest
        # to largest

        count = k
        res = root.val

        def dfs(node : Optional[TreeNode]):
            nonlocal count, res
            if not node:
                return
            dfs(node.left) # Go as far left as possible first
            count -= 1 # Decrement count after going as far left
            if count == 0:
                res = node.val # Update res
                return
            dfs(node.right) # Step right once each farthest left

        dfs(root)
        return res
