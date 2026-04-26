# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Traverse breadth-first and invert TreeNode.left and TreeNode.right

        if not root:
            return None
        stack = [] # BFS stack
        stack.append(root)
        start = root

        while stack:
            top = len(stack) - 1
            left = stack[top].left
            right = stack[top].right

            hold = stack[top].left
            stack[top].left = stack[top].right
            stack[top].right = hold
            if left:
                stack.append(left)
            if right:
                stack.append(right)
            stack.pop(top)
        
        return start