# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Solution 1: iterative BFS, queuing by level
        if not root:
            return []
        res = []
        stack = [] # Tracks current level
        res.append([root.val])
        stack.append(root)

        while stack: # Loops until all nodes searched
            level = [] # List of Nodes for next level
            vals = [] # List of Values for next level
            while stack: # Gets entire next level
                if stack[0].left:
                    level.append(stack[0].left)
                    vals.append(stack[0].left.val)
                if stack[0].right:
                    level.append(stack[0].right)
                    vals.append(stack[0].right.val)
                stack.pop(0)
            if vals: # Adds list of values from next level to res
                res.append(vals)
            # Sets stack to next level
            stack = level

        return res
