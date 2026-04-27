# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        if p.val != q.val:
            return False
        # Recursive DFS
        res = True

        def checkIsSame(p: Optional[TreeNode], q: Optional[TreeNode]) -> (int, int):
            nonlocal res
            if not p and not q:
                return 0, 0
            elif not p or not q:
                res = False
                return 0, 0
            
            (leftP, leftQ) = checkIsSame(p.left, q.left)
            (rightP, rightQ) = checkIsSame(p.right, q.right)

            if leftP != leftQ or rightP != rightQ:
                res = False
            
            return (p.val, q.val)
        
        checkIsSame(p, q)

        return res