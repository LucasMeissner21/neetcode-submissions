# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Traverse depth-first and invert TreeNode.left and TreeNode.right

        if not root:
            return None

        stack = [] # DFS stack
        stack.append(root)
        start = root

        while stack:
            top = len(stack) - 1 # uses top for DFS
            left = stack[top].left
            right = stack[top].right

            # Invert left and right
            stack[top].left = stack[top].right
            stack[top].right = left

            # Add new nodes to stack
            if left:
                stack.append(left)
            if right:
                stack.append(right)
            # Remove top of stack
            stack.pop(top)
        
        return start