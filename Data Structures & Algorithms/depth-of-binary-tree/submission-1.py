# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # First attempt, breadth first search
        if not root:
            return 0
        stack = [] # breadth first search stack
        stack.append(root)
        maxDepth = 0

        while stack:
            n = len(stack)
            # For each layer of the tree, add all children to stack while removing parents
            for i in range(n):
                if stack[0].left:
                    stack.append(stack[0].left)
                if stack[0].right:
                    stack.append(stack[0].right)
                stack.pop(0)
            # Inc maxDepth       
            maxDepth += 1

        return maxDepth