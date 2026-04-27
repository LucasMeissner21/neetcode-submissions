# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        stack = []
        res.append([root.val])
        stack.append(root)

        while stack:
            level = []
            vals = []
            while stack:
                if stack[0].left:
                    level.append(stack[0].left)
                    vals.append(stack[0].left.val)
                if stack[0].right:
                    level.append(stack[0].right)
                    vals.append(stack[0].right.val)
                stack.pop(0)
            if vals:
                res.append(vals)
            stack = level

        return res
