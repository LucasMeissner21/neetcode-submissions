# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Attempt 2: Recursive DFS, much more compact
        if not p and not q: # Base case
            return True
        
        if p and q and p.val == q.val: # Returns and'd left and right child recursive calls
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        else: # only one of p or q exist, or vals !=
            return False
        