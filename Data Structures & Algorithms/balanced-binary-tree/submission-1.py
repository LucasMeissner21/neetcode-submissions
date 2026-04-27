# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Recursive DFS with global res variable
        res = True

        # Recursive height - returning DFS function
        def getHeight(root: Optional[TreeNode]) -> int:
            nonlocal res
            # Base Case
            if not root: 
                return 0

            # recursive function call
            left = getHeight(root.left)
            right = getHeight(root.right)

            # Check for unbalanced tree
            if abs(left - right) > 1: # 
                res = False

            return 1 + max(left, right)
        
        # Call recursive function
        getHeight(root)

        return res