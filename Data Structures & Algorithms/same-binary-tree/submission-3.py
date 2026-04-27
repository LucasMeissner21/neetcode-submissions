# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Recursive DFS with global res
        if not p and not q: # If no inputs p or q
            return True
        elif not p or not q: # If only one input p or q
            return False
        if p.val != q.val: # If root's are not equal
            return False
        # Recursive DFS
        res = True

        # Recursive funciton
        def checkIsSame(p: Optional[TreeNode], q: Optional[TreeNode]) -> (int, int):
            nonlocal res
            if not p and not q:
                return 0, 0
            elif not p or not q: # If only one child node exists, trees are not equal
                res = False
                return 0, 0
            
            (leftP, leftQ) = checkIsSame(p.left, q.left)
            (rightP, rightQ) = checkIsSame(p.right, q.right)

            if leftP != leftQ or rightP != rightQ: # Check for equality
                res = False
            
            return (p.val, q.val)
        
        # Call recursive function
        checkIsSame(p, q)

        return res